import json
import pandas as pd
import sys
import trigger_methods as tm
import xlsxwriter

# Import Arguments
# total arguments
n = len(sys.argv)
 
# Arguments passed
try:
    file_name = sys.argv[1]
except:
    file_name = 'GTM-MVPNN2_workspace1000413.json'

try:
    export_file = sys.argv[2]
except:
    export_file = 'testing.xlsx'

    
# JSON to data frame
df = pd.read_json(file_name)
df2 = df.loc['trigger','containerVersion']
df3 = pd.DataFrame(df2)

# print(df3)

# customEventFilter parser
for index, row in df3.iterrows():
    customEventFilter_new = tm.event_parser(row['customEventFilter'], 'customEventFilter')
    n = 0
    try:
        column_name = 'customEventFilter_new_%s' % (n)
        df3.loc[index,'customEventFilter_new'] = customEventFilter_new[n]
        n += 1
    except:
        pass
    
# autoEventFilter parser
for index, row in df3.iterrows():
    autoEventFilter_new = tm.event_parser(row['autoEventFilter'], 'autoEventFilter')
    n = 0
    try:
        while n < len(autoEventFilter_new):
            column_name = 'autoEventFilter_new_%s' % (n)
            df3.loc[index,column_name] = autoEventFilter_new[n]
            n += 1
    except:
        pass

# Filter parser
for index, row in df3.iterrows():
    filter_new = tm.filter_parser(row['filter'])
    n = 0
    try:
        # print(filter_new)
        # print(len(filter_new))
        while n < len(filter_new):
            column_name = 'Filter_new_%s' % (n)
            df3.loc[index,column_name] = filter_new[n]
            n += 1
    except:
        pass

# Parameter Parser

for index, row in df3.iterrows():
    parameter_new = tm.parameter_parser(row['parameter'], row['type'])
    # print(row['type'])
    n = 0
    # print(parameter_new)
    try:
        df3.loc[index,'parameter_new'] = parameter_new
    except: 
        pass

# print(df3.loc[0])

# clean up columns and reorder
df4 = df3.drop(['filter','fingerprint','autoEventFilter','waitForTags','checkValidation','waitForTagsTimeout','uniqueTriggerId', 'customEventFilter'], axis=1)
last_col = len(df4.loc[0])
order = []
for i in range(last_col):
    if i != 5 and i != 6:
        order.append(i)
order += [5,6]

# print(order)
df_final = df4.iloc[:, order]


#Format workbook
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(export_file, engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object. Turn off the default
# header and index and skip one row to allow us to insert a user defined
# header.
df_final.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets['Sheet1']

# Get the dimensions of the dataframe.
(max_row, max_col) = df_final.shape

# Create a list of column headers, to use in add_table().
column_settings = []
for header in df_final.columns:
    column_settings.append({'header': header})

# Add the table.
worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})

# Make the columns wider for clarity.
worksheet.set_column(0, max_col - 1, 12)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
