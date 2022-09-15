# lists: ordered, mutable, allows duplicate values
# creating list
mylist=["banana",1,True, "apple", "man"]
print(mylist)

# creating empty list
mylist2=list()      #using list() function
print(mylist2)

# accessing using indexes
print(mylist[0])
print(mylist[-1])

# iterating over the list
for i in mylist:
    print(i)

#check if itme is present
if "banana" in mylist:
    print("yes")
else:
    print("no")

#number of elements
print(len(mylist))

# adding new element in the list at the end
mylist.append("lemon")
print(mylist)

# adding new element at specific position
mylist.insert(1,"berry")
print(mylist)

#pop last item
mylist.pop()
print(mylist)

# removing specific item
mylist.remove("man")
print(mylist)

# remove all elements with all methods
mylist.clear()
print(mylist)


mylist3=[3,7,2,8,0,1,34,87]
#reverse the list
mylist3.reverse()
print(mylist3)

#sort the array
mylist3.sort()
print(mylist3)

# creating new list with multiple same values
newlist=[2]*7
print(newlist)

# concatenate 2 list
nlist=[2,4,'ashu',True,4.8]
mlist=['qwe','pmd',False]

print(nlist+mlist)

#slicing: list_name[start_index:end_index
a=nlist[1:4]            # prints elements from 1 to 3
print(a)

b=nlist[:]              # prints all elements
print(b)

c=nlist[:4]             # from start index to 3
print(c)

d=nlist[2:]             # from 2 to end index
print(d)

e=nlist[::2]            # print every second element
print(e)

f=nlist[::-1]           #to reverse th list
print(f)

# copying list
nlistcpy=nlist.copy()
print(nlistcpy)

nl=list(nlist)      #second method
print(nl)

# list comprehension
lis=[1,2,3,4,5,6,7,8,9,10]
b=[x*x for x in lis]
print(b)

c=[x for x in lis if x%2==0 ]
print(c)




