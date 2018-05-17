import os
import ast

with open('id_list.txt', 'r') as id_file:
    handle = id_file.read()

id_list = ast.literal_eval(handle)
os_list = os.listdir()
id_list_pdb = [i + '.pdb' for i in id_list]
os_list = [i for i in os_list if i.endswith('.pdb')]

remaining = list(set(id_list_pdb) - set(os_list))
remaining = ['https://files.rcsb.org/download/' + i for i in remaining]
# remaining = [i[:-4] for i in remaining]

print(len(id_list))
print(len(os_list))
print(len(remaining))

import requests

print('Beginning file download with requests')

for url in remaining:
    r = requests.get(url)
    print(url)
    # Retrieve HTTP meta-data
    print(r.status_code)  
    # print(r.headers['content-type'])  
    # print(r.encoding)  