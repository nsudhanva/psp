# Author: (c) Sudhanva Narayana

# Import Pandas

import pandas as pd

file_names = ['102l_A', '1hq3_A', '1hq3_B', '1hq3_C', '1hq3_D', '1hq3_E', '1hq3_F', '1hq3_G', '1hq3_H']
fragment_writer = pd.ExcelWriter('fragment3.xlsx')

duplicates = []

for file_name_1 in file_names:
    pd_xlsx = pd.ExcelFile(file_name + '.xlsx')
    pd_df = pd.read_excel(pd_xlsx, 'fragment3')
    pd_df['ID'] = pd_df['Metadata'][0] 
    pd_df['Resolution'] = float(pd_df['Metadata'][1])
    pd_df.drop(columns=['Metadata'])
    duplicates.append(pd_df[pd_df.duplicated(['Fragments'], keep=False)])

result_df = pd.concat(duplicates)
result_df.to_excel(fragment_writer)

fragment_writer.save()