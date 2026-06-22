import numpy as np

arr = np.array([10,20,30,40,50])

print(arr)

#Dimensional Array
a = np.array(40)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3,4,5,6], [1,2,3,4,5,6]])
d = np.array([[[1,2,3], [1,2,3]], [[1,2,3], [1,2,3]]])

print(a, "\n", b, "\n", c, "\n", d) #Print Dimension
[]
print(a.ndim, b.ndim, c.ndim, d.ndim) #Know the dimension

print(b[2] + b[1]) #Print same dimension 1D
print(c[0,1] + c[1,2]) #Print same dimension 2D
print(c[0] + c[1,5]) #Print array + num 2D
print(c[0] + c[1]) #Print addition of array
print(d[0,1,0]) #Print num from 3D

#Slicing through
print(c[1::2])