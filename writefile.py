#append mode: adding new content in the file
file=open('file.txt','a')
#write mode:it overide the content of file
file=open("file.txt",'w')
file.write(".cricket is a good game")

#we can also use write mode to crete a new file
file=open("file1.html",'w')
file.write("<p>this is html</p>")

file.close()