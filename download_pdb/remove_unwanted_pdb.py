import ast
import os

with open('id_list.txt', 'r') as id_file:
    handle = id_file.read()

extension = '.pdb'
id_list = ast.literal_eval(handle)

id_list = [i + '.pdb' for i in id_list]
extra_id_list = os.listdir()
# print(len(extra_id_list))

extra_id_list = [i for i in extra_id_list if i.endswith(extension)]

delete_list = list(set(extra_id_list) - set(id_list))

# print(len(id_list))
# print(len(extra_id_list))
# print(len(delete_list))

for i in delete_list:
    os.remove(i)
    print(i)
