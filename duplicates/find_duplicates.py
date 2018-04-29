# Author: (c) Sudhanva Narayana

# Import Pandas

import pandas as pd

file_names = ['102l_A', '1hq3_A', '1hq3_B', '1hq3_C', '1hq3_D', '1hq3_E', '1hq3_F', '1hq3_G', '1hq3_H']
fragment_writer = pd.ExcelWriter('fragment3.xlsx')

duplicates = []

for i in range(len(file_names)):
    for j in range(i, len(file_names)):
        # print(file_names[i], file_names[j])
        pd_xlsx_1 = pd.ExcelFile(file_names[i] + '.xlsx')
        pd_xlsx_2 = pd.ExcelFile(file_names[j] + '.xlsx')

        pd_df_1 = pd.read_excel(pd_xlsx_1, 'fragment3')
        pd_df_2 = pd.read_excel(pd_xlsx_2, 'fragment3')

        pd_df_1['ID'] = pd_df_1['Metadata'][0] 
        pd_df_2['ID'] = pd_df_2['Metadata'][0] 
        pd_df_1['Resolution'] = float(pd_df_1['Metadata'][1])
        pd_df_2['Resolution'] = float(pd_df_2['Metadata'][1])

        pd_df_1.drop(columns=['Metadata'])
        pd_df_2.drop(columns=['Metadata'])

print(pd_df_1['Fragments'] == pd_df_2['Fragments'])

for file_name in file_names:
    pd_xlsx_1 = pd.ExcelFile(file_name + '.xlsx')
    pd_xlsx_2 = pd.ExcelFile(file_name + '.xlsx')
    pd_df = pd.read_excel(pd_xlsx, 'fragment3')
    pd_df['ID'] = pd_df['Metadata'][0] 
    pd_df['Resolution'] = float(pd_df['Metadata'][1])
    pd_df.drop(columns=['Metadata'])
    duplicates.append(pd_df[pd_df.duplicated(['Fragments'], keep=False)])

result_df = pd.concat(duplicates)
result_df.to_excel(fragment_writer)

fragment_writer.save()