# SETS: unordered, mutable, no duplicate
mysets={1,2,3,4,5,6,7,2,1,8}
print(mysets)

#EMpty set
mset=set()
print(mset)

# find the number of element in set
print(len(mysets))

#adding new element
mysets.add(12)
mysets.add(10)
mysets.add(111)
mysets.add(144)

print(mysets)


#removing elements
mysets.remove(3)
print(mysets)

#OR
mysets.discard(4)
print(mysets)

# deleting element
print(mysets.pop())             #remove arbitary element of the sets

# iterating through sets
for i in mysets:
    print(i)

#check if element is present in sets
if 100 in mysets:
    print("yes")
else:
    print("no")
# Clear the sets
mysets.clear()
print(mysets)