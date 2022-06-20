import GTM_Trigger_Decoder as td
import pandas as pd
import os

from trigger_methods import folder_dictionary

def audit(file_dir,output_dir, auto_open, output_filename):
    # declarations
    export_file = output_dir+'//' + output_filename + '.xlsx'
    df = pd.read_json(file_dir)
    
    # print(df)
    try:
        folder_dic = folder_dictionary(df.loc['folder','containerVersion'])
    except:
        print('Dictionary failed')
    trigger_df = td.trigger_decoder(df, folder_dic)

   
    # print(type(export_file))
    # print(export_file)
    #Format workbook
    writer = pd.ExcelWriter(export_file, engine='xlsxwriter')
    trigger_df.to_excel(writer, sheet_name='Triggers', startrow=1, header=False, index=False)
    workbook = writer.book
    worksheet = writer.sheets['Triggers']
    (max_row, max_col) = trigger_df.shape
    column_settings = []
    for header in trigger_df.columns:
        column_settings.append({'header': header})
    worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})
    worksheet.set_column(0, max_col - 1, 12)
    writer.save()
    
    if auto_open == 1:
            os.startfile(export_file)

# # Test conditions
# file_dir = 'GTM-MVPNN2_workspace1000413 (4).json'
# output_dir = os.path.expanduser('~\downloads')
# auto_open = 1


# audit(file_dir,output_dir, auto_open)