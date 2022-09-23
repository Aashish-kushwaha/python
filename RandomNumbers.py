import random

a=random.random()       # it gives random float values between 0 to 1
print(a)

# to get number between specific range
b=random.uniform(1,10)      # random float between 1-10
print(b)

# random integer number between the given range
c=random.randint(1,10)
print(c)

d=random.randrange(1,10) # upper bound is not included
print(d)

#
e=random.normalvariate(0,1)         #this will pick the random value from the normal distribution with the mean 0 and standard deviation of 1
print(e)

# function to work with sequences
mylist=list("abcdefgh")
h=random.choice(mylist)
print(h)

# pick more than one element
li=list("dhfhdheue")
k=random.sample(li,3)
print(k)


# shuffling
l2=list("difrhfjkd")
random.shuffle(l2)
print(l2)

import secrets

#used for passwords, security
# disadvantgaes is that it is slow

a=secrets.randbelow(10)     #random number between 0 and 10 where 10 is not included
print(a)

b=secrets.randbits(3)       # this gives us k bits  like in case 7 is highest number which we can get
print(b)

