def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return -1
        
    return 1
       
            
num=int(input("enter number:"))
for i in range(2,num+1):
    if(prime(i)==1):
        print(i)
