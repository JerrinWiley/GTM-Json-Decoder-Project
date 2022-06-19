import GTM_Trigger_Decoder as td
import pandas as pd
import os

def audit(file_dir,output_dir, auto_open):
    # print(auto_open)

    # Arguments passed
    try:
        file_name = file_dir
        # print(file_name)
    except:
        print('Incorrect file:')
        print(file_name)

    # print('file_name: ' + file_name)
    # print('file_name w/o path: ', os.path.basename(file_name))
    export_file = output_dir+'//'+os.path.basename(file_name)[:-5] + '_cleaned.xlsx'

    df = pd.read_json(file_dir)

    trigger_df = td.trigger_decoder(df)

   
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