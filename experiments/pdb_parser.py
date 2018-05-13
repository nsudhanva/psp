import Bio.PDB
from Bio.PDB import *

parser_1 = PDBParser()
parser_2 = PDBParser()
parser_3 = PDBParser()
structure_1 = parser_1.get_structure("test1", '102l.pdb')
structure_2 = parser_2.get_structure("test2", '104l.pdb')
structure_3 = parser_3.get_structure("test2", '103m.pdb')
chain_name_1 = 'A'
chain_name_2 = 'A'
chain_name_3 = 'A'
chain_1 = structure_1[0][chain_name_1]
chain_2 = structure_2[0][chain_name_2]
chain_3 = structure_3[0][chain_name_2]

print(list(chain_1)[41:44])
print(list(chain_2)[40:43])
# print(list(chain_3))
print(list(chain_3)[0:3])

print(len(list(chain_3)))


# hello = [1, 2, 3, 4, 5, 6, 7]
# print(hello[0:3])
# print(hello[1:3])
# print(hello[3:6])
# print(hello[3:7])
# print(hello[4:6])
# print(hello[4:7])
