from natsort import natsorted, ns
import re
atom = ['1', '10', '100', '1000', '2']
num = [3, 4, 5, 1, 2, 3]
natsorted(atom, key=lambda y: y.lower())
# atom.sort()
num.sort()
print(num)
print(atom)