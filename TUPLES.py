# tuples: ordered, immutable, allows duplicate elements
mytuple=("ashu",2,"kush")
print(mytuple)

#single value tuple
mytupl2=("max",)            # if we do not put comma it will be treated as string
print(type(mytupl2))
print(mytupl2)

# using tuple function
mytuple3=tuple(["max",2,"skd",True])
print(mytuple3)

# indexing
item=mytuple3[2]
print(item)
print(mytuple3[-1])

#iterating
for x in mytuple3:
    print(x)

# checking if element is present in tuple
if "tim" in mytuple3:
    print("yes")
else:
    print("no")

mytuple4=('a','b','c','d','e','a')

#number of elemnt
print(len(mytuple4))

#count number of occuring of elemnet
print(mytuple4.count('a'))
print(mytuple4.count(1))        #0

# find the index or first occurrence of elements
print(mytuple4.index('c'))
print(mytuple4.index('c'))

#convert tuple to list
LIST=list(mytuple4)
print(LIST)
print(type(LIST))

#convert list o tuple
t=tuple(LIST)
print(t)
print(type(t))

tup=(1,2,3,4,5,6,7,8,9)

# slicing
a=tup[2:7]
print(a)

b=tup[:8]
print(b)

c=tup[2:]
print(c)

d=tup[::-1]         # trick to reverse tuple
print(d)

# PACKING:when we create a tuple , we normally assign value o it. this is called "packing" a tuple
fruits=("apple","banana","cherry")

# UNPACKING: when we extract the values back into vaiabes. this is called unpacking
f1,f2,f3=fruits
print(f1)
print(f2)
print(f3)

#using *
fruit = ("apple", "banana", "cherry", "strawberry", "raspberry")
f1,f2,*f3=fruit;            #assign rest of the values accept "apple" and "banana" to f3 as list
print(f1)
print(f2)
print(f3)
print(type(f3))

f1,*f2,f3=fruit
print(f1)
print(f2)
print(f3)