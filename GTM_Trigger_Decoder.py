from sqlite3 import Row
import pandas as pd
import trigger_methods as tm

def trigger_decoder(df, folder_dict):        
    # JSON to data frame
    df2 = df.loc['trigger','containerVersion']
    df3 = pd.DataFrame(df2)

    # print(df3)

    # customEventFilter parser
    for index, row in df3.iterrows():
        try:
            customEventFilter_new = tm.event_parser(row['customEventFilter'], 'customEventFilter')
        except:
            pass
        n = 1
        try:
            while n <= len(customEventFilter_new):
                column_name = 'Custom Event Filter %s' % (n)
                # print(column_name)
                df3.loc[index,column_name] = customEventFilter_new[n-1]
                # print(df3.loc[index,column_name])
                n += 1
        except:
            pass
        
    # autoEventFilter parser
    for index, row in df3.iterrows():
        try:
            autoEventFilter_new = tm.event_parser(row['autoEventFilter'], 'autoEventFilter')
        except:
            pass
        n = 0
        try:
            while n < len(autoEventFilter_new):
                column_name = 'Auto Event Filter %s' % (n+1)
                df3.loc[index,column_name] = autoEventFilter_new[n]
                n += 1
        except:
            pass

    # Filter parser
    for index, row in df3.iterrows():
        try:
            filter_new = tm.filter_parser(row['filter'])
        except:
            pass
        n = 0
        try:
            # print(filter_new)
            # print(len(filter_new))
            while n < len(filter_new):
                column_name = 'Filter %s' % (n+1)
                df3.loc[index,column_name] = filter_new[n]
                n += 1
        except:
            pass

    # Parameter Parser

    for index, row in df3.iterrows():
        try:
            parameter_new = tm.parameter_parser(row['parameter'], row['type'])
        except:
            pass
        # print(row['type'])
        n = 0
        # print(parameter_new)
        try:
            df3.loc[index,'parameters'] = parameter_new
        except: 
            pass

    # Apply folder names
    for index, row in df3.iterrows():
        try:
            folder_name = folder_dict[row.loc['parentFolderId']]
            df3.loc[index, 'Folder Name'] = folder_name
        except:
            pass

    # clean up columns and reorder
    drop_filters = ['filter','fingerprint','autoEventFilter','waitForTags','checkValidation','waitForTagsTimeout','uniqueTriggerId', 'customEventFilter','parameter']
    for filter in drop_filters:
        try:
            df3 = df3.drop([filter], axis=1)
        except:
            pass

    last_col = len(df3.loc[0])
    order = []
    for i in range(last_col):
        if i != 5 and i != 6:
            order.append(i)
    order += [5,6]

    # print(order)
    df_final = df3.iloc[:, order]
    return df_final