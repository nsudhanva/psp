# strings = ['first',  'first',  'first', 'second', 'third', 'third', 'fourth', 'first', 'first', 'first', 'third', 'third']

# what i want -> ['first', 'second', 'third', 'fourth', 'first', 'third']

strings = ['MET', 'MET', 'MET', 'MET', 'MET', 'MET', 'MET', 'MET', 'ASN', 'ASN', 'ASN', 'ASN', 'ASN', 'ASN', 'ASN', 'ASN', 'ILE', 'ILE', 'ILE', 'ILE', 'ILE', 'ILE', 'ILE', 'ILE', 'PHE', 'PHE', 'PHE', 'PHE', 'PHE', 'PHE', 'PHE', 'PHE', 'PHE', 'PHE', 'PHE', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'MET', 'MET', 'MET', 'MET', 'MET', 'MET', 'MET', 'MET', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ILE', 'ILE', 'ILE',
'ILE', 'ILE', 'ILE', 'ILE', 'ILE', 'ASP', 'ASP', 'ASP', 'ASP', 'ASP', 'ASP', 'ASP', 'ASP', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLY', 'GLY', 'GLY', 'GLY', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'ARG', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU', 'LYS', 'LYS', 'LYS', 'LYS', 'LYS', 'LYS', 'LYS', 'LYS', 'LYS', 'ILE', 'ILE', 'ILE', 'ILE', 'ILE', 'ILE', 'ILE', 'ILE', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'LYS', 'LYS', 'LYS', 'LYS', 'LYS', 'LYS', 'LYS', 'LYS', 'LYS', 'ASP', 'ASP', 'ASP', 'ASP', 'ASP', 'ASP', 'ASP', 'ASP', 'THR', 'THR', 'THR', 'THR', 'THR', 'THR', 'THR', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLU', 'GLY', 'GLY', 'GLY', 'GLY', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'TYR', 'THR', 'THR', 'THR', 'THR', 'THR', 'THR', 'THR']

occurances = [7, 15, 23, 34, 43, 51, 59, 70, 78, 86, 95, 99, 107, 118, 126, 135, 143, 155, 164, 172, 179, 188, 192, 204, 216, 223]

j = 0

for i in occurances:
    print(strings[j:i + 1])
    j = i + 1

