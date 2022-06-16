import json
import csv
import pandas as pd


# Initializations
file_name = "GTM-MVPNN2_workspace1000413.json"

# JSON to data frame
df = pd.read_json(file_name)
df2 = df.loc['trigger','containerVersion']
df3 = pd.DataFrame(df2)
df4 = df3.sort_values(by=['name'])
row = 0

while row < len(df4):
    l = df4.loc[row, 'filter']
    n = 1
    try:
        for i in l:
#             print(i)
            string = str('')
            string += i['type']
            q = 1
            for j in i['parameter']:
        #         print(j)
                if q < 2:
                    string = j['value'] + ' '  + string
                elif q > 2:
                    pass
                else:
                    string += ' ' + j['value']
                q += 1
    #         print(string)
            column_name = 'filter ' + str(n)
    #         print(column_name)
            df4.loc[row, column_name] = string
            n += 1
    except:
#         print(row)
#         print('missing')
        pass
    row += 1
row = 0

while row < len(df4):
    try:
        string = ''
        l = df4.loc[row, 'customEventFilter'][0]
        k = df4.loc[row, 'customEventFilter'][0]['type']
        i = 0
        string = df4.loc[row, 'customEventFilter'][0]['parameter'][0]['value'] + ' ' + df4.loc[row, 'customEventFilter'][0]['type'] + ' ' + df4.loc[row, 'customEventFilter'][0]['parameter'][1]['value']
        df4.loc[row, 'eventFilter'] = string
    except:
        pass
    row += 1
df5 = df4.drop(['filter','fingerprint','autoEventFilter','waitForTags','checkValidation','waitForTagsTimeout','uniqueTriggerId', 'customEventFilter'], axis=1)
df_final = df5.iloc[:, [0,1,2,3,4,9,7,8,5,6]]
df_final.to_csv('testing2.csv')