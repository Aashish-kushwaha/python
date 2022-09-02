import numpy
import numpy as np

#using lsit for the creation of array
arr=np.array([1,2,3])
print("array of rank 1:\n",arr)
#array of rank 2
arr=np.array([[1,2,3],
          [4,5,6]])
print("array of rank 2:\n",arr)
#array using tuple
arr=np.array((1,2,3))
print("array using tuple:\n",arr)


#using numpy.arrange:creates array with regularly incrementing values.
arr=np.arange(10)
print("array:\n",arr)

print()

arr=np.arange(3,10, dtype=float)
print("array:\n",arr)

arr=np.arange(2,3,0.1)
print("array:\n",arr)

#using numpy.linspace:creates array with the specified number of elements

arr=np.linspace(2,3,5)
print("array:\n",arr)

#creting multidimensional array
#method 1st

list1=[1,2,3]
list2=[3,4,5]
list3=[6,7,8]

arr=np.array([list1,list2,list3])
print("multidimensional array1:\n",arr)
print(arr.__sizeof__())

#method 2nd
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("multidimensional array2:\n",a)
print(a.shape)

#creating empty array
arr=np.empty([4,3])
print("empty array:\n",arr)

#using numpy.ones
arr=numpy.ones([4,3],dtype=int,order='f')
print("array:\n",arr)

#using numpy.zeros
arr=np.zeros([3,3],dtype=int)
print("array:\n",arr)
print(arr.__sizeof__())

#get dimension
print("dimension:",arr.ndim)
#get shape
print("shape:",arr.shape)
#dtype
print("data type:",arr.dtype)
#get item size
print("item size:",arr.itemsize)
#get total size
print("total size:",arr.nbytes)


