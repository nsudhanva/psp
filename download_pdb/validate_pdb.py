import ast
import os

with open('id_list.txt', 'r') as id_file:
    handle = id_file.read()

# handle = "['1hq3', 'abcd', '104l']"

id_list = ast.literal_eval(handle)
pdb_error_list = []

count = 0
for file_name in id_list:
    try:
        with open(file_name + '.pdb', 'r') as pdb_file:
            pdb = pdb_file.read()
          
        pdb = pdb.split()

        # print(pdb[-1:])
        if len(pdb) > 0:
            if pdb[-1:][0] != 'END':
                pdb_error_list.append(file_name)
                os.remove(file_name + '.pdb')
                # print(str(count) + " ", end="")
            else:
                pass
        count = count + 1

    except Exception as e:
        pass
  
with open('invalid_pdbs.txt', 'w') as invalid_handle:
    invalid_handle.write(str(pdb_error_list))
    