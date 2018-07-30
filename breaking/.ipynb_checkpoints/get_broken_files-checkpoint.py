import os
broken_files_chain = os.listdir()
suffix = '.xlsx'
broken_files_chain = [i for i in broken_files_chain if i.endswith(suffix)]
broken_files_chain = [i[:-5] for i in broken_files_chain]
# print(broken_files_chain)

with open('broken_files_chain.txt', 'w') as broken_files:
    broken_files.write(str(broken_files_chain))