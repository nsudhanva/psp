# Author: (c) Sudhanva Naryana

import ast
import pandas as pd

id_list = []
url_list = []
df = pd.DataFrame()

with open('id_list.txt', 'r') as id_file:
    handle = id_file.read()

id_list = ast.literal_eval(handle)
# print(len(id_list))

for id in id_list:
    url_list.append('https://files.rcsb.org/download/' + str(id))

# Write all files to txt
with open('url_list.txt', 'a') as url_file:
    url_file.write(str(url_list))

df['ID'] = pd.Series(id_list)
df['URLS'] = pd.Series(url_list)
df.to_csv('ids.csv')