print("please select operation-:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("select operation from 1, 2, 3, 4:")
n=int(input())
print("enter first number:")
n1=int(input())
print("enter second number:")
n2=int(input())

if n==1:
    print(n1+n2)
elif n==2:
    print(n1-n2)
elif n==3:
    print(n1*n2)
elif n==4:
    print(n1/n2)
    
