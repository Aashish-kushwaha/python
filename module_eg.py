def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

print("file name:%s" %__name__)

  
if __name__ == "__main__": 
    print ("File1 is being run directly")
else: 
    print ("File1 is being imported")