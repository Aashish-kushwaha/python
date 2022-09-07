#opening file in read mode
file=open("file.txt",'r')           #storing all the content of file in file variable
print(file.readable())              #to check if file is readable
print(file.read())                  #prints every thing present in the file
print(file.readline())                 #read the first line
print(file.readline())                  #read the second line
print(file.readlines())                 #this function take everyline and put them into a list and then we can print which ever line we want
print(file.readlines()[0])              #reads the first line of the file

#we can also use for loop and readlines to display the contentt of file
for lines in file.readlines():
    print(lines)

#it is recommended to close file in the end of the program
file.close()
'''
#writing file
open("file.txt",'w')
#append file
open("file.txt",'a')
'''