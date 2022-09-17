# Strings: ordered, immutable, text representation

# creating strings
my_strings='Hell\'o\'world'
print(my_strings)
my_strings2="hello python"
print(my_strings2)

# accessing character in the strings
ch=my_strings[1]
print(ch)
ch2=my_strings[-1]
print(ch2)

# length or number of character in a string
print(len(my_strings))
# slicing
substring=my_strings[1:6]           # to get the substring
print(substring)
s1=my_strings[:]                    # print whole string
print(s1)

s2=my_strings[3:]                    # to get the substring from 3 to end
print(s2)

s3=my_strings[:12]                      # to get the substring from starting to 12
print(s3)

print(my_strings[11])

# to reverse the string
s4=my_strings[::-1]
print(s4)

# to get every second element
print(my_strings[::2])

# concatenation of string
greeting="hello"
name="tom"
sentence=greeting+name
print(sentence)

#iterating through string
for i in my_strings:
    print(i)

# checking if character is present in the string
if 'p' in my_strings:
    print("yes")
else:
    print("no")


# removing white spaces
s5="    hello tom your   cat is cute    "
s5=s5.strip()       # strip() methods removes any leading and trailing characters by default that character is space
print(s5)

# convert every character to upper case
print(my_strings.upper())

# convert every character to lower case
print(my_strings.lower())

# check if string start with some character
print(my_strings.startswith('p'))

# checking if string end with some character
print(my_strings.endswith("d"))

# find the first index of character
print(my_strings.find('o'))

# replace character or substring
print(my_strings.replace('world','universe'))          # if it does not find the string to be replaced it simply do nothing and print the same old string

# convert string to list
s7="how are you"
my_list=s7.split()          #split() method splits a string into a list, we can specify the separator, default separator is whitespace
print(my_list)

# formatting string: there are two types of formatting string first is using  % sign and second is using  format method and also there are f=String
var="tom"
s8="the variable is %s" % var  # here  % tells compiler that there is a string placeholder
print(s8)

# using format method
var="tom"
s9="the variable is {}".format(var)
print(s9)

# using f-String
var="tom"
v2=3.4
v3=7
s10=f"the variables is {var} and {v2} and {v3}"
print(s10)
