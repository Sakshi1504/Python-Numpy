import numpy as np

a=np.matrix("1 2; 4 5")
b=np.matrix([[1,2],[4,5]])

print(a)
print(b)

print(a+b)

print(a)
print(b)

print(a*b)

print(a)
print(b)


print(a)
print(b)

print(np.transpose(a))
print(a.transpose())
print("here", b.T)