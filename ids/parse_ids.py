# Author: (c) Sudhanva Naryana

import xml.etree.ElementTree as ET
tree = ET.parse('getCurrent.xml')
root = tree.getroot()

ids = []
url_list = []

# Get list of all files at RCSB
for child in root:
    ids.append(child.attrib['structureId'])
    url_list.append('https://files.rcsb.org/download/' + child.attrib['structureId'])

with open('id_list.txt', 'a') as id_file:
    id_file.write(str(ids))

# Write all files to txt
with open('url_list.txt', 'a') as url_file:
    url_file.write(str(url_list))