# collection : counter, namedtuple, OrderedDict,deque, default dict
"""
COLLECTION: the collection module in python provides types of containers.
A container is an object that is used to store different objects.
E.g:counters, OrderedDIct, DefaultDict, ChainMap, Deque

Counter: counter is a subclass of dict. therefore it is an unordered collection
where elements and their respective count are stored as a dictionary.

"""
from collections import Counter

a="asjdjwqjejda"
my_counter = Counter(a)
print(my_counter)

# to get the key-value pair
i=my_counter.items()
print(i)
print(type(i))

# to get all the keys
print(my_counter.keys())

# to get all the values
print(my_counter.values())


# most common element in the dictionary
print(my_counter.most_common(1))            # number argue is the number of most common element

# elements() is one of the functions of counter class, when invoked on the counter object
# will return an itertool of all the known counter object

print(list(my_counter.elements()))
for x in my_counter.elements():
    print(x)

"""
namedtuple: namedtuple contains keys that are hashed to a particular value
this container is just like Dictionary is that it supports both access from key-value and iteration
"""
from collections import namedtuple
# declaring namedtuple
point=namedtuple('point','x,y')
#adding value
pt=point(1,-2)
print(type(point))
# accessing using name
print(pt)
print(pt.x,pt.y)
print(type(pt))
print(type(pt.x))

student=namedtuple('student',('name','age','dob'))
s=student('tom','12','12-9-2020')
print(s)

for x in s:
    print(x)

"""OrderedDict: an OrderedDict is a dictionary subclass that remembers the order that
keys were first inserted. the only difference between dict() and OrderedDict is thet 
Ordered dict preserves the order in which the keys are inserted
"""
from collections import OrderedDict
ordered_dict=OrderedDict()
ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']="name"
ordered_dict['d']=True
ordered_dict['e']=5

print(ordered_dict)

