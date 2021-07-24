import numpy as np


a=np.matrix([[1,2],[3,4]])
print(a)
#inverse of a matrix
print(np.linalg.inv(a))

#power of a matrix - n>0

print(np.linalg.matrix_power(a,2))

#n=0 - power of matrix

print(np.linalg.matrix_power(a,0))

#n<0 - power of matrix

print(np.linalg.matrix_power(a,-2))

#linear alebra - a= square matrix-coefficients

b=np.array([1,2])

print(np.linalg.solve(a,b))



arn=np.array([[6,2,-5],[3,3,-2],[7,5,-3]])
brn=np.array([13,13,26])
print(np.linalg.solve(arn,brn))

#determinant

print(np.linalg.det(a))
print(round(np.linalg.det(a)))

print(np.linalg.det(arn))
print(round(np.linalg.det(arn)))