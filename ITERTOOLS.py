"""
itertools: itertools is a module in python, it is used to iterate over data structure that can be stepped over
using a for-loop. such data structures are also known as iterables.
itartools provide some adcance tools like product, permutation, combination, groupby,infinite iterator
"""
from itertools import product,permutations,combinations,accumulate,combinations_with_replacement,groupby
import operator
a=[1,2,3]
b=[4,5,6]
prod=product(a,b)
print(prod)
print(type(prod))
print(list(prod))

#PERMUTATION: A permutation is a collection or a combination of objects from as set where the order or the arrangement of teh chosen objects does matter.import
a=[1,2,3,4]
perm=permutations(a)
print((list(perm)))

#COMBINATION: the combination function takes two arguement- an iterable inputs and a positive n- and produces an iterator over tuples of all combinations of n elements in inputs.
a=[1,2,3,4]
comb=combinations(a,2)
print(list(comb))

#combination_with_replacement:it work just like combination the only difference is that it allows element to be repeated in the tuples it returns
a=[1,2,3,4]
combr=combinations_with_replacement(a,2)
print(list(combr))

#ACCUMULATE:this iterator takes two arguements, iterable target and function which would be followed at each iteration of value in targe. by default taht function is addition
a=[1,2,3,4]
acc=accumulate(a)
print(a)
print(list(acc))
acc1=accumulate(a, func=operator.mul)       # to get the multiplication
print(a)
print(list(acc1))

b=[1,2,5,6,3]
acc2=accumulate(b, func=max)
print(list(acc2))


#GROUPBY: this method calculat ethe keys for each element present in iterable. it returns key and iterable of grouped items
def smaller_than(x):
    return x<3


a=[1,2,3,4]
group_obj=groupby(a,key=smaller_than)
for key,value in group_obj:
    print(key,list(value))

# same function using lamda function
group_obj=groupby(a,key=lambda x:x<3)
for key,value in group_obj:
    print(key,list(value))

persons=[{"name":"tim","age":25},{"name":"tom","age":25},{"name":"tem","age":55},{"name":"kim","age":35}]

group_obj=groupby(persons, key=lambda x: x["age"])
for key,value in group_obj:
    print(key,list(value ))