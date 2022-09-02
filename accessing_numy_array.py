import numpy as np
import random
arr=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print("array:\n",arr)

#getting the specific element using indexing
print(arr[1,5])

#getting the specific row

print("first row:",arr[0,:])

#getiing the specific column

print("third column:",arr[:,2])

#little fancy
#like getting the value from 2 to 6 with the difference of 2

print(arr[0,1:6:2])
#or
print(arr[0,1:-1:2])

#3-D matrix
brr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3-D matrix:\n",brr)

print(brr[0,1,2])

#initializing the arrays

#iniitializing with zero
a1=np.zeros((((3,6,2,3))))
print(a1)

#initializing with 1
a2=np.ones((2,3))
print(a2)

#initializing with any other number
a3=np.full((2,2),33)
print(a3)
print()
#random decimal numers
a4=np.random.rand(4,3)
print(a4)
print()
#the identity matrix
a6=np.identity(4)
print(a6)
'''
create the following matrix
1 1 1 1 1 
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1
'''
a7=np.ones((5,5))
print(a7)
a8=np.zeros((3,3))
print(a8)
a8[1,1]=9
print(a8)
a7[1:-1,1:-1]=a8
print(a7)
print()
#coying array
a9=np.array([1,2,3])
b1=a9.copy()        #this way the new b1 matrix is created
print(b1)

#basic mathematics
print("basic mathematics on an array")
a10=np.array([1,2,3,4])
print(a10)
print("additon:",a10+2)
print("subtraction:",a10-2)
print("multiply:",a10*3)
print("divide:",a10/2)
print("power:",a10**2)

b2=np.array([5,6,7,8])
print("adding two matrix:",a10+b2)

print("sin of elevry element:",np.sin(a10))
print()
print("cos of every element:",np.cos(a10))


#linear algebra
a11=np.ones((2,3))
print(a11)
b3=np.full((3,2),2)
print(b3)
print(np.matmul(a11,b3))