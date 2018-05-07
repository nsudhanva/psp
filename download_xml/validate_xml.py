import xml.etree.ElementTree as ET

file_name = '1hq3'

try:
    tree = ET.parse(file_name + '.xml')
except ET.ParseError:
     with open('xml_errors.txt', 'a') as error_file:
            error_file.write(str(file_name + '.xml') + "\n")