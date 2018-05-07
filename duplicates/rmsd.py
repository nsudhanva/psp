import Bio.PDB
from Bio.PDB.PDBParser import PDBParser
import pandas as pd

fragment = pd.read_excel('fragment3.xlsx')
print(fragment.head()) 

parser = PDBParser()
structure = parser.get_structure("test", "102l.pdb")
atoms = structure.get_atoms()
residues_1 = structure.get_residues()
residues_2 = structure.get_residues()

# print(list(residues_1))
# print(list(residues_2))
# for i in residues:
    # print(list(i))
    # print(i.get_resname(), i.get_full_id()[3][1])
    # print(i.get_segid())
    # break

temp_1 = list(residues_1)[42:45]
temp_2 = list(residues_2)[134:137]

print(temp_1)
print(temp_2)

atoms_1 = []
atoms_2 = []

for i in temp_1:
    # print(i.get_full_id()[3][1])
    print(list(i.get_atoms()))
    atoms_1 = atoms_1 + list(i.get_atoms())

for j in temp_2:
    # print(i.get_full_id()[3][1])
    print(list(j.get_atoms()))    
    atoms_2 = atoms_2 + list(j.get_atoms())

print(len(atoms_1))
print(len(atoms_2))

fixed = atoms_1
moving = atoms_2
# moving = list(atoms)[0:21]
# print(atoms_1)

sup = Bio.PDB.Superimposer()
sup.set_atoms(fixed, moving)
print(sup.rms)
sup.apply(moving)
print(sup.rms)