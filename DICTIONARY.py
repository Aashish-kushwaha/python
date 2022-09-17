# Dictionary: key-value pairs, Unordered, mutable
# Creating dictionary
mydict={"name":"max","age":28,"city":"dehradun"}
print(mydict)

# using dict function
mydict2=dict(name="mary",age=27,city="bostong")
print(mydict2)

# accessing values
value=mydict["name"]
print(value)
value2=mydict["age"]
print(value2)

# adding new key-value pair
mydict["email"]="max@gmail.com"
print(mydict)

# delete key-value pair
del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

# checking if element is present in dictionary
if "name" in mydict:
    print("yes")
else:
    print("no")

# iterating through dictionary
for k in mydict2:
    print(k)            # print all the key

for k in mydict2.keys():
    print(k)            #print key of dictionary

for k in mydict2.values():
    print(k)

# copy of dictionary
newdict=dict(mydict2)
print(newdict)


