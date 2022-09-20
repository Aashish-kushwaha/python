#Errors and EXCEPTION
"""
ERRORS: errors are the problems in a program due to which the program will stop th execution
EXCEPTION: Exceptions are raised when some interval events occur which changes the normal flow of the program

types of error:
-> syntax error: when the proper syntax of the language is not followed then a syntax error is thrown.
-> logical errors(Exception):

"""

# syntax error
#a=(s))          #this produces syntax error

# Exception
#TypeError:occurs when an operation is applied to an object of inappropriate type.
#a=30+'sd'

#ImportError: an ImportError is raised when the import statement is unable to load a module
#import module
#NameError: this error is raised when a local or global name is not found.
#a=5
#b=c
#FileNotFoundError: file is not found
#f=open('somefile.txt')
#ValueError: a ValueError is raised when a built-in operation or function receives an arguement taht has the right type but an invalid value
#a=[1,2,3,4]
#a.remove(5)
#IndexError: list index out of range
a=[1,2,3,4,5]
print(a[9])
#keyerror

#raise
#assertionerror
#handle exception
#try and except
