import numpy as np

x = np.ones((8, 8))
print('Before:')
print(x)

b = np.zeros((6,6))
x[1:7,1:7] = b

print('After:') 
print(x)