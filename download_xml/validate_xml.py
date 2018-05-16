import xml.etree.ElementTree as ET
import ast
import os

with open('id_list.txt', 'r') as id_file:
    handle = id_file.read()

id_list = ast.literal_eval(handle)
xml_error_list = []

for file_name in id_list:
    try:
        tree = ET.parse(file_name + '.xml')
    except Exception:
        try:
            os.remove(file_name + '.xml')
            xml_error_list.append(file_name)
        except Exception as e:
            # print(file_name)
            pass

with open('xml_errors.txt', 'a') as error_file:
    error_file.write(str(xml_error_list) + "\n")