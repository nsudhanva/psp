# Author: (c) Sudhanva Naryana

# Import Element Tree for XML Parsing, Pandas, CSV

import xml.etree.ElementTree as ET
import pandas as pd
import csv   

# File tree
tree = ET.parse('102l.xml')

# Root contains parsed, encoded XML 
root = tree.getroot()

# Excel Writer
writer = pd.ExcelWriter('sample5.xlsx', engine='xlsxwriter')

# Element Dictionary
elemDict = {}

for elem in tree.iter():
    elemDict[elem.tag[42:]] = elem.text 

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

    # Converting DataFrames to List
    auth_seq_list = list(auth_seq_df)
    auth_comp_list = list(auth_comp_df)
    auth_atom_id_list = list(auth_atom_id_df)
    cartn_x_list = list(cartn_x)
    cartn_y_list = list(cartn_y)
    cartn_z_list = list(cartn_z)

    # Final Series Lists
    seq_list = []
    start_list = []
    end_list = []
    final_cartn_x_list = []
    final_cartn_y_list = []
    final_cartn_z_list = []
    final_auth_atom_id_list = []

    # Starting Fragment
    start = auth_seq_list[0]
    count = 0
    # Sequence length
    seq = fragment

    # Occurances of Sequence changes
    occurances = []
    atom_ids = []

    # Creating occurances with Sequence list
    for i in auth_seq_list:
        occurances.append(len(auth_seq_list) - 1 - auth_seq_list[::-1].index(i))

    occurances = list(set(occurances))
    occurances.sort()

    list_index = 0

    # Final DataFrame
    final_seq_df = pd.DataFrame()

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

    # Creating final sequence
    for i in range(0, len(auth_temp_list)):
        seq_list.append(''.join(auth_temp_list[i:i + fragment]))
        start_list.append(i + 1)
        end_list.append(i + fragment)          

    # Appending all lists to DataFrame by converting them to Series
    final_seq_df['Fragments'] = pd.Series(seq_list)
    final_seq_df['Start'] = pd.Series(start_list)
    final_seq_df['End'] = pd.Series(end_list)
    final_seq_df['Atom IDs'] = pd.Series(final_auth_atom_id_list)
    final_seq_df['X'] = pd.Series(final_cartn_x_list)
    final_seq_df['Y'] = pd.Series(final_cartn_y_list)
    final_seq_df['Z'] = pd.Series(final_cartn_z_list)
    final_seq_df['Metadata'] = pd.Series(['102l', resolution])

    # Printing the head of final DataFrame
    print(final_seq_df.head())

    # Creating the excel with Sheets 
    final_seq_df.to_excel(writer, sheet_name='fragment' + str(fragment))

# Saving the writer
writer.save()