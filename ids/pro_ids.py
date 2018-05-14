with open('protein_id_list.txt', 'r') as id_file:
    handle = id_file.read()

# print(handle)

lists = handle.split()
lists = set(lists)
lists = [i for i in lists if len(i) == 4]

print(len(lists))