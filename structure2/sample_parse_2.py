import xml.etree.ElementTree as ET
import pandas as pd
import csv

tree = ET.parse('102l.xml')
root = tree.getroot()

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

# print(str(df_dict)[-1000:])
# print(df_dict['atom_siteCategory'])
# print(str(df_dict['atom_siteCategory'])[:1000])
df = pd.DataFrame(df_dict['atom_siteCategory']).transpose()
df['Resolution'] = elemDict['ls_d_res_high']
# print(type(df.index))
df.index.name = 'ids'
df.index = df.index.map(int)
# print(type(df.index))
df.sort_index()
# print(df.head())
# df.to_csv('sample2.csv')

auth_seq_df = df.iloc[:, 7]
auth_comp_df = df.iloc[:, 6]

# auth_seq_beg = auth_seq_df.iloc[:10]
# print(auth_seq_df)
# print(list(auth_seq_df))

auth_seq_list = list(auth_seq_df)
auth_comp_list = list(auth_comp_df)

start = auth_seq_list[0]
count = 0
seq = 3

occurances = []

for i in auth_seq_list:
    occurances.append(len(auth_seq_list) - 1 - auth_seq_list[::-1].index(i) )

occurances = list(set(occurances))
occurances.sort()
# print(occurances)
final_seq_df = pd.DataFrame()
# print(enumerate(auth_comp_list))
# print(auth_comp_list)

seq_list = []
start_list = []
end_list = []
# print(seq_series)

for index, value in enumerate(auth_comp_list):
    # print(index)
    if index + 2 < len(occurances):
        seq_list.append(auth_comp_list[occurances[index]] + auth_comp_list[occurances[index + 1]] + auth_comp_list[occurances[index + 2]])
        start_list.append(index + 1) # just index
        end_list.append(index + 3) # just index + 2

# print(seq_list)

final_seq_df['Fragments'] = pd.Series(seq_list)
final_seq_df['Start'] = pd.Series(start_list)
final_seq_df['End'] = pd.Series(end_list)
print(final_seq_df.head())

# print(seq_series)

# for index, value in enumerate(auth_comp_list):
#     # print(index, value)
#     # break
#     if index + 2 < len(occurances):
#         # seq_list.append(auth_comp_list[occurances[index]] + auth_comp_list[occurances[index + 1]] + auth_comp_list[occurances[index + 2]])
#         seq_list.append(''.join(list(set(auth_comp_list[:occurances[index + 2]]))))

#         start_list.append(index + 1) # just index
#         end_list.append(index + 3) # just index + 2