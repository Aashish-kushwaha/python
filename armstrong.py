def armstrong(n):
    x = 0
    while n != 0:
        r = n % 10
        x = r * r * r + x
        n = n // 10

    return x;


n = int(input("enter number:"))
r1 = armstrong(n)
if n == r1:
    print("number is armstrong")
else:
    print("number is not a armstrong")
