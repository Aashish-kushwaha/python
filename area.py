import math
def sq_area(side):
    return side*side

def rec_area(l,b):
    return l*b

def c_area(r):
    return 3.14*r*r

def tri_area(a,b,c):
    s=(a+b+c)/3
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

print("select from the following :")
print("1 for square:")
print("2 for rec_area:")
print("3 for circle:")
print("4 for square:")
n=int(input())
if(n==1):
    s=int(input("enter the side of square:"))
    print("area of square:",sq_area(s))
elif(n==2):
    l=int(input("enter length:"))
    b=int(input("enter breadth:"))
    print("area of square:",rec_area(l,b))
elif n==3:
    r=int(input("enter the radius of circle:"))
    print("area of square:",c_area(r))
elif n==4:
    a=int(input("enter first side:"))
    b=int(input("enter second side:"))
    c=int(input("enter third side:"))
    print("area of square:",c_area(a,b,c))



    
