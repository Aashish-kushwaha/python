def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n1 = int(input("enter number"))
n2 = factorial(n1)
print(n2)
