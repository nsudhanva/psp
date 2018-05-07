import numpy as np 
import math

X_1 = np.array([10, 20, 30])
X_2 = np.array([40, 20, 30])

Y_1 = np.array([14, 20, 30])
Y_2 = np.array([10, 24, 34])

Z_1 = np.array([10, 40, 30])
Z_2 = np.array([10, 70, 36])

X = (X_1 - X_2) ** 2
Y = (Y_1 - Y_2) ** 2
Z = (Z_1 - Z_2) ** 2

print(math.sqrt((X + Y + Z).mean()))
print(X, Y, Z)