arr=[]
n=int(input("enter number of input:"dir
            ))
for i in range(0,n):
    no=int(input())
    arr.append(no)

print(arr)

max=arr[0]
for i in range(1,n):
    if(arr[i]>max):
        max=arr[i]

print(max)

