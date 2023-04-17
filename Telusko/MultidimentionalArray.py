from numpy import *
"""
arr1=array ([

    [1,2,3],
    [5,6,7]
])

print(arr1.dtype)
print(arr1.shape)
print(arr1.size)
"""
"""
arr1=array([
    [1,2,3,4,5,6],
    [9,8,7,6,5,4]
])

arr2=arr1.flatten()  # it change the 2D array Into 1D array

arr3=arr1.reshape(3,4)

print(arr2)
print(arr3)

"""





# matices

"""
arr1=array([
    [1,2,3,4],
    [5,6,7,8]
])

m=matrix(arr1)
print(m)

"""

"""
m=matrix('1,2,3;5,6,7;8,9,10')
print(m)
print(diagonal(m))
print(m.min())
print(m.diagonal())

"""


m1=matrix('1,2,3;4,5,6;7,8,9')
m2=matrix('4,3,2;7,6,5;9,8,7')

m3=m1+m2
m4=m1*m2
print(m3)
print(m4)

