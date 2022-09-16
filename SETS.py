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


odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7,11}

#union
u=odds.union(evens)
print(u)

#intersection
i=odds.intersection(evens)
print(i)

#difference of two sets
setA={1,2,3,4,5,6,7,8,9}
setB={4,5,6,1,7,3}

diff=setA.difference(setB)
print(diff)
#symetric difference
d=setA.symmetric_difference((setB))
print(d)

#subset
print(setB.issubset(setA))
#superset
print(setA.issuperset(setB))

