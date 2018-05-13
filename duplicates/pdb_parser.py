import Bio.PDB
from Bio.PDB import *

parser_1 = PDBParser()
parser_2 = PDBParser()
structure_1 = parser_1.get_structure("test1", '102l.pdb')
structure_2 = parser_2.get_structure("test2", '104l.pdb')
chain_name_1 = 'A'
chain_name_2 = 'A'
chain_1 = structure_1[0][chain_name_1]
chain_2 = structure_2[0][chain_name_2]

print(list(chain_1)[:5])
print(list(chain_2)[:5])