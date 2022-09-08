def compound_interest(p, r, t):
    c = p * (pow((1 + r / 100), t))
    return c - p


p = int(input("enter the principal amount:"))
r = float(input("enter the rate of interest:"))
t = float(input("enter the time period:"))

print("compound interest:", compound_interest(p, r, t))
