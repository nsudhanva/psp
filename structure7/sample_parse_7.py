# Author: (c) Sudhanva Narayana

# Import Element Tree for XML Parsing, Pandas, CSV

import xml.etree.ElementTree as ET
import pandas as pd
import csv   
from collections import Counter

# File tree
file_name = '1hq3'
tree = ET.parse(file_name + '.xml')

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
    chain_occurances_start = []

    chain_index = 0

    for i in auth_seq_list[:-1]:
        if int(auth_seq_list[chain_index]) > int(auth_seq_list[chain_index + 1]):
            chain_occurances.append(chain_index)
            # print(chain_index)
        else:
            chain_occurances_start.append(chain_index)
        chain_index = chain_index + 1

    chain_occurances.append(int(chain_index))

    for i, v in enumerate(chain_occurances):
        chain_occurances[i] = chain_occurances[i] + i
    # print(chain_occurances)
    chain_occurances_start = [x + 2 for x in chain_occurances]
    chain_occurances_start.insert(0, 1)
    chain_occurances_start.pop()
    print(chain_occurances_start)
    
# print(chains_list)

# Excel Writer
writer = []
main_index = 0
temp_start = 0

for chain, ci, ci_start in zip(chains_list, chain_occurances, chain_occurances_start):
    writer.append(pd.ExcelWriter(file_name + '_' + chain + '.xlsx', engine='xlsxwriter'))

    # For fragment in 3 to 41 fragments
    for fragment in range(3, 42):
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
        
        chain_seq_start = 0
        tempo_auth_seq_list = auth_seq_list
        tempo_auth_comp_list = auth_comp_list
        tempo_auth_atom_id_list = auth_atom_id_list
        tempo_cartn_x_list = cartn_x_list
        tempo_cartn_y_list = cartn_y_list
        tempo_cartn_z_list = cartn_z_list
        tempo_auth_asym_id_list = auth_asym_id_list
        tempo_auth_asym_id = auth_asym_id

        auth_seq_list = tempo_auth_seq_list[chain_seq_start:ci]
        auth_comp_list = tempo_auth_comp_list[chain_seq_start:ci]
        auth_atom_id_list = tempo_auth_atom_id_list[chain_seq_start:ci]
        cartn_x_list = tempo_cartn_x_list[chain_seq_start:ci]
        cartn_y_list = tempo_cartn_y_list[chain_seq_start:ci]
        cartn_z_list = tempo_cartn_z_list[chain_seq_start:ci]
        auth_asym_id_list = tempo_auth_asym_id_list[chain_seq_start:ci]
        auth_asym_id = tempo_auth_asym_id[chain_seq_start:ci]
        
        # print(auth_asym_id)
        # Check for unique elements
        unique_asym_id = unique_list(auth_asym_id_list)
        # print(unique_asym_id)

        # Final Series Lists
        seq_list = []
        end_list = []
        final_cartn_x_list = []
        final_cartn_y_list = []
        final_cartn_z_list = []
        final_auth_atom_id_list = []
        start_list = []

        # Starting Fragment
        start = int(auth_seq_list[temp_start])
        count = 0
        # print(start)

        # Sequence length
        seq = fragment

        # Occurances of Sequence changes
        occurances = []
        atom_ids = []

        # print(auth_seq_list)

        # Creating occurances with Sequence list
        for i in auth_seq_list:
            occurances.append(len(auth_seq_list) - 1 - auth_seq_list[::-1].index(i))

        occurances = list(set(occurances))
        occurances.sort()

        list_index = 0

        # Final DataFrame
        final_seq_df = pd.DataFrame()

        auth_temp_list = []
        j = 0

        # Creating temporary sequence list
        for i in occurances:
            auth_temp_list.append(unique_list(auth_comp_list[j:i + 1])[0])
            j = i + 1

        # Temporary Lists
        auth_temp_atom_id_list = []
        temp_cartn_x_list = []
        temp_cartn_y_list = []
        temp_cartn_z_list = []

        # Creating temporary Lists
        j = 0
        for i in occurances:
            auth_temp_atom_id_list.append(auth_atom_id_list[j:i + 1])  
            temp_cartn_x_list.append(cartn_x_list[j:i+1])
            temp_cartn_y_list.append(cartn_y_list[j:i+1])
            temp_cartn_z_list.append(cartn_z_list[j:i+1])
            j = i + 1

        # Creating final lists
        for i in range(0, len(auth_temp_atom_id_list)):
            # Combining all lists into a single list
            temp_auth = [item for sublist in auth_temp_atom_id_list[i:i + fragment] for item in sublist] 
            temp_auth_x = [item for sublist in temp_cartn_x_list[i:i + fragment] for item in sublist] 
            temp_auth_y = [item for sublist in temp_cartn_y_list[i:i + fragment] for item in sublist] 
            temp_auth_z = [item for sublist in temp_cartn_z_list[i:i + fragment] for item in sublist] 
            final_cartn_x_list.append(temp_auth_x)
            final_cartn_y_list.append(temp_auth_y)
            final_cartn_z_list.append(temp_auth_z)
            final_auth_atom_id_list.append(temp_auth)

        type_list = []
        type_list_occurances = []

        # Creating final sequence
        for i in range(0, len(auth_temp_list)):
            seq_list.append(''.join(auth_temp_list[i:i + fragment]))
            type_list.append(auth_temp_list[i:i + fragment])

        # print(auth_temp_list)

        # Creating start and end list
        for i in range(start - 1, len(auth_temp_list) + (start - 1)):
            start_list.append(i + 1)
            # print(i + 1)
            end_list.append(i + fragment) 
            # print(i + fragment)
            
        for i in type_list:
            type_list_occurances.append(dict(Counter(i)))

        # print(auth_temp_list)
        # print(type_list)
        # print(type_list_occurances)

        # Appending all lists to DataFrame by converting them to Series
        final_seq_df['Fragments'] = pd.Series(seq_list)
        final_seq_df['Start'] = pd.Series(start_list)
        final_seq_df['End'] = pd.Series(end_list)
        final_seq_df['Atom IDs'] = pd.Series(final_auth_atom_id_list)
        final_seq_df['X'] = pd.Series(final_cartn_x_list)
        final_seq_df['Y'] = pd.Series(final_cartn_y_list)
        final_seq_df['Z'] = pd.Series(final_cartn_z_list)
        final_seq_df['Type'] = pd.Series(type_list_occurances)
        final_seq_df['Metadata'] = pd.Series([file_name, resolution])

        # Printing the head of final DataFrame
        # print(final_seq_df.head())
        n = fragment - 1
        final_seq_df = final_seq_df[:-n]
        # Creating the excel with Sheets 
        final_seq_df.to_excel(writer[main_index], sheet_name='fragment' + str(fragment))
        # print(chain_seq_start)
        chain_seq_start = ci
        # print(ci)
        final_seq_df.drop(final_seq_df.index, inplace=True)
        
        # print(start_list[-1])
        # print(end_list[-1])
        # start = end_list[-1]
        # break
    # Saving the writer
    writer[main_index].save()
    main_index = main_index + 1
    # break