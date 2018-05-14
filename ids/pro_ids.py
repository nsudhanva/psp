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
    url_list.append('https://files.rcsb.org/download/' + str(id) + '.pdb')

# Write all files to txt
with open('pdb_url_list.txt', 'w') as url_file:
    for url in url_list:
        url_file.write(str(url) + '\n')