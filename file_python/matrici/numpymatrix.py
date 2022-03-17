import numpy as np

A = np.array([[1, 4, 5, 12], 
				[-5, 8, 9, 0],
					[-6, 7, 11, 19]])

print("A[:,0] =",A[:,0]) # First Column
print("A[:,1] =", A[:,1]) # Fourth Column
print("A[:,2] =", A[:,2]) # Last Column (4th column in this case)
print("A[:,2] =", A[:,3])
