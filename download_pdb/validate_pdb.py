import ast

# with open('id_list.txt', 'r') as id_file:
#     handle = id_file.read()

handle = "['1hq3', 'abcd', '104l']"

id_list = ast.literal_eval(handle)
pdb_error_list = []

for file_name in id_list:
    with open(file_name + '.pdb', 'r') as pdb_file:
        pdb = pdb_file.read()
    
    pdb = pdb.split()

     # print(pdb[-1:])
    if len(pdb) > 0:
        if pdb[-1:][0] != 'END':
            pdb_error_list.append(file_name)
        else:
            # print(file_name)
            pass
            
with open('invalid_pdbs.txt', 'w') as invalid_handle:
    invalid_handle.write(str(pdb_error_list))