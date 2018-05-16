# Author: (c) Sudhanva Narayana

import Bio.PDB
import numpy as np
import pandas as pd
import ast
import os

ROOT_DIR = os.path.dirname(os.path.abspath('__file__'))
PARENT_DIR = os.path.abspath(os.path.join(ROOT_DIR, os.pardir))
BROKEN_DIR = os.path.abspath(PARENT_DIR + '\\' + 'breaking')

with open(BROKEN_DIR + '\\' + 'broken_files_chain.txt', 'r') as broken_chain_file:
    file_handle = broken_chain_file.read()

try:
    file_names = ast.literal_eval(file_handle)
except Exception as e:
    file_names = []

for frag in range(1, 42):
    fragment_writer = pd.ExcelWriter('fragment' + str(frag) + '.xlsx')
    print("Fragment: ", frag)
    duplicates = []
    result_df = pd.DataFrame()
    test_df = pd.DataFrame()

    for i in range(len(file_names)):
        for j in range(i, len(file_names)):
            # print(file_names[i], file_names[j])

            pd_xlsx_1 = pd.ExcelFile(BROKEN_DIR + '\\' + file_names[i] + '.xlsx')
            pd_xlsx_2 = pd.ExcelFile(BROKEN_DIR + '\\' + file_names[j] + '.xlsx')

            pd_df_1 = pd.read_excel(pd_xlsx_1, 'fragment' + str(frag))
            pd_df_2 = pd.read_excel(pd_xlsx_2, 'fragment' + str(frag))

            pd_df_1['ID'] = pd_df_1['Metadata'][0] 
            pd_df_2['ID'] = pd_df_2['Metadata'][0] 

            try:
                pd_df_1['Resolution'] = float(pd_df_1['Metadata'][1])
                pd_df_2['Resolution'] = float(pd_df_2['Metadata'][1])
            except Exception as e:
                pd_df_1['Resolution'] = float(0)
                pd_df_2['Resolution'] = float(0)
                # print(e)
                pass

            for seq1 in range(len(pd_df_1['Fragments'])):
                for seq2 in range(seq1 + 1 if file_names[i] == file_names[j] else 0, len(pd_df_2['Fragments'])):
                    if (pd_df_1['Fragments'][seq1] == pd_df_2['Fragments'][seq2]):
                        test_df = pd.DataFrame({'Fragments_1': [pd_df_1['Fragments'][seq1]], 'Start_1': [pd_df_1['Start'][seq1]], 'End_1': [pd_df_1['End'][seq1]], 'Fragments_2': [pd_df_2['Fragments'][seq2]], 'Start_2': [pd_df_2['Start'][seq2]], 'End_2': [pd_df_2['End'][seq2]], 'Resolution_1': [pd_df_1['Resolution'][0]], 'Resolution_2': [pd_df_2['Resolution'][0]], 'ID_1' : [file_names[i]], 'ID_2' : [file_names[j]], 'Atoms_1': [pd_df_1['Atom IDs'][seq1]], 'X_1': [pd_df_1['X'][seq1]], 'Y_1': [pd_df_1['Y'][seq1]], 'Z_1': [pd_df_1['Z'][seq1]], 'Atoms_2': [pd_df_2['Atom IDs'][seq2]], 'X_2': [pd_df_2['X'][seq2]], 'Y_2': [pd_df_2['Y'][seq2]], 'Z_2': [pd_df_2['Z'][seq2]]})
                        result_df = pd.concat([result_df, test_df], ignore_index=True)
                            
    #        break
    #    break
                        
    result_df = result_df[['ID_1', 'Fragments_1', 'Start_1', 'End_1', 'Atoms_1', 'X_1', 'Y_1', 'Z_1' , 'Resolution_1', 'ID_2', 'Fragments_2', 'Start_2', 'End_2', 'Atoms_2', 'X_2', 'Y_2', 'Z_2', 'Resolution_2']]
    result_df.to_excel(fragment_writer)
    fragment_writer.save()