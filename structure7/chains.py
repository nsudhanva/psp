# Author: (c) Sudhanva Naryana

# Import Element Tree for XML Parsing, Pandas, CSV

import xml.etree.ElementTree as ET
import pandas as pd
import csv   
from collections import Counter

# File tree
tree = ET.parse('1hq3.xml')

# Root contains parsed, encoded XML 
root = tree.getroot()

# Element Dictionary
elemDict = {}

for elem in tree.iter():
    elemDict[elem.tag[42:]] = elem.text 

# Function to create a Unique List (Remove Duplicates)
def unique_list(strings):
    new_strings = []

    if len(strings) == 1:
        new_strings.append(strings[0])
        return new_strings

    for index, value in enumerate(strings):
        if index == len(strings) - 1:
            new_strings.append(value)
            break

        if strings[index] != strings[index + 1]:
            new_strings.append(value)

    # Returns a list of unique strings
    return new_strings

# Dictionary for DataFrame, Grand Child DataFrame, Grand Grand Child DataFrame
df_dict = {}
df_g_child_dict = {}
df_g_child_ids = []
df_gg_child_dict = {}

# For every child in root
for child in root:
    df_g_child_dict = {}
    # For every Grand Child in Child
    for g_child in child:
        # Dictionary for Grand Grand Child DataFrame
        df_gg_child_dict = {}


        # For every Grand Grand Child in Child
        for gg_child in g_child:        
            df_gg_child_dict[gg_child.tag[42:]] = gg_child.text

        df_g_child_dict[int(g_child.attrib['id'])] = df_gg_child_dict

    df_dict[child.tag[42:]] =  df_g_child_dict
    break

# print(df_dict)

# Original DataFrame
df = pd.DataFrame(df_dict['atom_siteCategory']).transpose()
# Resolution
resolution = elemDict['ls_d_res_high']

df.index.name = 'ids'
df.index = df.index.map(int)
df.sort_index()

# Sequence, Composition and Atoms
auth_seq_df = df.iloc[:, 7]
auth_comp_df = df.iloc[:, 6]
auth_atom_id_df = df.iloc[:, 5]

# X, Y, Z values
cartn_x = df.iloc[:, 1]
cartn_y = df.iloc[:, 2]
cartn_z = df.iloc[:, 3]

# A, B, C...
auth_asym_id = df.iloc[:, 4]
group_pdb = df.iloc[:, 8]
# print(df.head())

# Converting DataFrames to List
group_pdb_list = list(group_pdb)
group_pdb_list = [x for x in group_pdb_list if x == 'ATOM']
group_pdb_list_length = len(group_pdb_list)

auth_seq_list = list(auth_seq_df[:group_pdb_list_length])
auth_comp_list = list(auth_comp_df[:group_pdb_list_length])
auth_atom_id_list = list(auth_atom_id_df[:group_pdb_list_length])
cartn_x_list = list(cartn_x[:group_pdb_list_length])
cartn_y_list = list(cartn_y[:group_pdb_list_length])
cartn_z_list = list(cartn_z[:group_pdb_list_length])
auth_asym_id_list = list(auth_asym_id[:group_pdb_list_length])
auth_asym_id = list(auth_asym_id[:group_pdb_list_length])

# print(auth_asym_id)
# Check for unique elements
unique_asym_id = unique_list(auth_asym_id_list)
# print(unique_asym_id)

# Final Series Lists
seq_list = []
start_list = []
end_list = []
final_cartn_x_list = []
final_cartn_y_list = []
final_cartn_z_list = []
final_auth_atom_id_list = []

# print(auth_seq_list)

if not len(auth_asym_id) == len(set(auth_asym_id)):
    chains_list = list(set(auth_asym_id))
    chains_list.sort()
    # print(chains_list)
    chain_occurances = []

    chain_index = 0

    for i in auth_seq_list[:-1]:
        if int(auth_seq_list[chain_index]) > int(auth_seq_list[chain_index + 1]):
            chain_occurances.append(chain_index + 1)
        chain_index = chain_index + 1

    chain_occurances.append(int(chain_index))
    # print(chain_occurances)
# print(chains_list)