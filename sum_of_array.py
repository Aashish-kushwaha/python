arr=[]
sum=0;
n=int(input("enter number of element in the list:"))
for i in range(0,n):
    v=int(input())
    arr.append(v)
    sum=sum+arr[i]

print(arr)
print(sum)
