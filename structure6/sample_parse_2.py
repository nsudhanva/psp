# Author: (c) Sudhanva Naryana

import xml.etree.ElementTree as ET
import pandas as pd
import csv

tree = ET.parse('1hq3.xml')
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
df.to_csv('sample2-AB.csv')

