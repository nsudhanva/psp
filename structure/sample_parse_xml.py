import xml.etree.ElementTree as ET
import pandas as pd
import csv

tree = ET.parse('102l.xml')
root = tree.getroot()

# res = root.findall('{http://pdbml.pdb.org/schema/pdbx-v50.xsd}ls_d_res_high')

# print(res)

elemDict = {}

for elem in tree.iter():
    elemDict[elem.tag[42:]] = elem.text 
    # print(elem.tag[42:], elem.attrib)

print(elemDict)
# # now I remove duplicities - by convertion to set and back to list
# elemList = list(set(elemList))

# # res = 'ls_d_res_high' in elemList
# # Just printing out the result
# # for ele in elemList:
# # # print(elemList)
# #     print(ele)

with open('samplexml.txt', 'a') as id_file:
    id_file.write(str(elemDict))