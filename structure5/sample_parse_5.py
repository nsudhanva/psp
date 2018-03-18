import xml.etree.ElementTree as ET
import pandas as pd
import csv

tree = ET.parse('102l.xml')
root = tree.getroot()
writer = pd.ExcelWriter('sample5.xlsx', engine='xlsxwriter')

elemDict = {}

for elem in tree.iter():
    elemDict[elem.tag[42:]] = elem.text 

df_dict = {}
df_g_child_dict = {}
df_g_child_ids = []
df_gg_child_dict = {}
# count = 0
# columns = []

# print(root)

for child in root:
    # print(child.tag[42:], child.attrib)
    
    df_g_child_dict = {}
    for g_child in child:
        # print('\t' + g_child.tag[42:], g_child.attrib)
        # print(g_child.attrib)
        df_gg_child_dict = {}
        for gg_child in g_child:
            # print('\t\t' + gg_child.tag[42:], gg_child.attrib, gg_child.text)
        
            df_gg_child_dict[gg_child.tag[42:]] = gg_child.text
            # break

        df_g_child_dict[int(g_child.attrib['id'])] = df_gg_child_dict
        # print(df_g_child_dict)   
        # count = count + 1

        # if count == 3:      
        #     break    
            
    df_dict[child.tag[42:]] =  df_g_child_dict
    break

for fragment in range(3, 42):
    # print(str(df_dict)[-1000:])
    # print(df_dict['atom_siteCategory'])
    # print(str(df_dict['atom_siteCategory'])[:1000])
    df = pd.DataFrame(df_dict['atom_siteCategory']).transpose()
    resolution = elemDict['ls_d_res_high']
    # print(type(df.index))
    df.index.name = 'ids'
    df.index = df.index.map(int)
    # print(type(df.index))
    df.sort_index()
    # print(df.head())
    # df.to_csv('sample2.csv')
    # print(resolution)

    auth_seq_df = df.iloc[:, 7]
    auth_comp_df = df.iloc[:, 6]
    auth_atom_id_df = df.iloc[:, 5]

    cartn_x = df.iloc[:, 1]
    cartn_y = df.iloc[:, 2]
    cartn_z = df.iloc[:, 3]

    # auth_seq_beg = auth_seq_df.iloc[:10]
    # print(auth_seq_df)
    # print(list(auth_seq_df))

    auth_seq_list = list(auth_seq_df)
    auth_comp_list = list(auth_comp_df)
    auth_atom_id_list = list(auth_atom_id_df)

    cartn_x_list = list(cartn_x)
    cartn_y_list = list(cartn_y)
    cartn_z_list = list(cartn_z)

    final_cartn_x_list = []
    final_cartn_y_list = []
    final_cartn_z_list = []

    # print(len(cartn_x_list))
    # print(len(auth_atom_id_list))

    final_auth_atom_id_list = []

    start = auth_seq_list[0]
    count = 0
    seq = fragment

    occurances = []
    atom_ids = []

    for i in auth_seq_list:
        occurances.append(len(auth_seq_list) - 1 - auth_seq_list[::-1].index(i))
        # atom_ids.append(len(auth_atom_id_list) - 1 - auth_atom_id_list[::-1].index(i))

    occurances = list(set(occurances))
    occurances.sort()
    # print(occurances)

    list_index = 0

    # print(auth_atom_id_list)

    # print(len(final_auth_atom_id_list))

    final_seq_df = pd.DataFrame()

    # print(enumerate(auth_comp_list))
    # print(auth_comp_list)

    seq_list = []
    start_list = []
    end_list = []

    # print(seq_series)

    def unique_list(strings):
            
        # print(len(strings))
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

        # print(new_strings)
        return new_strings


    # print(auth_comp_list)
    auth_temp_list = []

    # print(auth_temp_list)

    # print(occurances)
    occur_index = 0

    j = 0

    for i in occurances:
        # print(auth_comp_list[j:i + 1])
        auth_temp_list.append(unique_list(auth_comp_list[j:i + 1])[0])
        j = i + 1

    # print(auth_atom_id_list)

    j = 0
    auth_temp_atom_id_list = []
    temp_cartn_x_list = []
    temp_cartn_y_list = []
    temp_cartn_z_list = []

    for i in occurances:
        # print(auth_atom_id_list[j:i + 1])  
        auth_temp_atom_id_list.append(auth_atom_id_list[j:i + 1])  
        temp_cartn_x_list.append(cartn_x_list[j:i+1])
        temp_cartn_y_list.append(cartn_y_list[j:i+1])
        temp_cartn_z_list.append(cartn_z_list[j:i+1])
        j = i + 1

    # print(len(auth_temp_atom_id_list))
    # print(len(auth_temp_list))

    for i in range(0, len(auth_temp_atom_id_list)):
        # print(i, i + 3)
        # print(auth_temp_atom_id_list[i:i + 3])
        temp_auth = [item for sublist in auth_temp_atom_id_list[i:i + fragment] for item in sublist] 
        temp_auth_x = [item for sublist in temp_cartn_x_list[i:i + fragment] for item in sublist] 
        temp_auth_y = [item for sublist in temp_cartn_y_list[i:i + fragment] for item in sublist] 
        temp_auth_z = [item for sublist in temp_cartn_z_list[i:i + fragment] for item in sublist] 
        final_cartn_x_list.append(temp_auth_x)
        final_cartn_y_list.append(temp_auth_y)
        final_cartn_z_list.append(temp_auth_z)
        final_auth_atom_id_list.append(temp_auth)

    for i in range(0, len(auth_temp_list)):
        # print(auth_temp_list[i:i + 3])
        seq_list.append(''.join(auth_temp_list[i:i + fragment]))

        start_list.append(i + 1)
        end_list.append(i + fragment)  
        # final_auth_atom_id_list.append(auth_atom_id_list[i])
        

    # print(seq_list)

    # print(start_list)
    # print(end_list)
    # print(final_auth_atom_id_list)

    final_seq_df['Fragments'] = pd.Series(seq_list)
    final_seq_df['Start'] = pd.Series(start_list)
    final_seq_df['End'] = pd.Series(end_list)
    final_seq_df['Atom IDs'] = pd.Series(final_auth_atom_id_list)
    final_seq_df['X'] = pd.Series(final_cartn_x_list)
    final_seq_df['Y'] = pd.Series(final_cartn_y_list)
    final_seq_df['Z'] = pd.Series(final_cartn_z_list)
    final_seq_df['Metadata'] = pd.Series(['102l', resolution])

    # print(final_seq_df.head())
    final_seq_df.to_excel(writer, sheet_name='fragment' + str(fragment))

writer.save()