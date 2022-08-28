def simple_interest(p,r,t):
    return (p*r*t)/100

p=int(input("enter the principal amount:"))
r=int(input("enter the rate of interest:"))
t= int(input("enter the time period:"))

print("simple interest:",simple_interest(p,r,t))
