# Author: (c) Sudhanva Naryana

import xml.etree.ElementTree as ET
import pandas as pd
import csv

tree = ET.parse('4zpy.xml')
root = tree.getroot()
df_dict = {}
df_g_child_dict = {}
df_gg_child_dict = {}
df = pd.DataFrame()

print(root)

for child in root:
    # print(child.tag[42:], child.attrib)
    
    for g_child in child:
        # print('\t' + g_child.tag[42:], g_child.attrib)

        for gg_child in g_child:
            # print('\t\t' + gg_child.tag[42:], gg_child.attrib, gg_child.text)
            df_gg_child_dict[gg_child.tag[42:]] = gg_child.text
            # df = pd.DataFrame(df_gg_child_dict)   
            df.to_csv('sample.csv')
            # print(df_gg_child_dict) 
            break

        df_g_child_dict[g_child.tag[42:]] = df_gg_child_dict
        # print(df_g_child_dict)             
        break    
            
    df_dict[child.tag[42:]] =  df_g_child_dict
    break
# df.append(df_dict)
print(df_dict)
# df.to_csv('sample.csv')