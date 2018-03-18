# Author: (c) Sudhanva Naryana

import xml.etree.ElementTree as ET
import pandas as pd
import csv

tree = ET.parse('102l.xml')
root = tree.getroot()

elemDict = {}

for elem in tree.iter():
    elemDict[elem.tag[42:]] = elem.text 

print(elemDict)

with open('samplexml.txt', 'a') as id_file:
    id_file.write(str(elemDict))