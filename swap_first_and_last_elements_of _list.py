ls=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    a=int(input())
    ls.append(a)

print("before swaping:"),
print(ls)

temp=ls[0]
ls[0]=ls[-1]
ls[-1]=temp

print("after swapping:"),
print(ls)
