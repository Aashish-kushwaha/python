# Errors and EXCEPTION
"""
ERRORS: errors are the problems in a program due to which the program will stop th execution
EXCEPTION: Exceptions are raised when some interval events occur which changes the normal flow of the program

types of error:
-> syntax error: when the proper syntax of the language is not followed then a syntax error is thrown.
-> logical errors(Exception):

"""

# syntax error
# a=(s))          #this produces syntax error

# Exception
# TypeError:occurs when an operation is applied to an object of inappropriate type.
# a=30+'sd'

# ImportError: an ImportError is raised when the import statement is unable to load a module
# import module
# NameError: this error is raised when a local or global name is not found.
# a=5
# b=c
# FileNotFoundError: file is not found
# f=open('somefile.txt')
# ValueError: a ValueError is raised when a built-in operation or function receives an arguement taht has the right type but an invalid value
# a=[1,2,3,4]
# a.remove(5)
# IndexError: list index out of range
# a=[1,2,3,4,5]
# print(a[9])
# keyError: raised when mapping key is not found in the existing key
# d={"1":"ashu","2":"dhruv","3":"krishna"}
# print(d["7"])

# Raising an exception: when we want to force exception after meeting certain condition
# x=-5
# if x<0:
#   raise Exception("x should be positive")

# assert in python: assertion is the boolean expression that checks if the statement
# is True and False. if the statement is true then it does nothing and continues the execution,
# but if statement is false then it stops the execution of the program and throws an error.from
# x=-5
# assert (x>=0), 'x is positive'

"""
handle exception: Try and Except satement are used to catch and handle exceptions in python. 
statement that can raise exception are kept inside the Try clause and the statements
taht handle the exception are written inside except clause
STRUCTURE OF TRY CATCH
try:
    some code that may raise exception
except:
    optional block
    used for handling exception if required
else:
    execute if no exception
finally:
     always executed
"""
# try and except
try:
    a = 5 / 0
except:
    print("an error")

try:
    a = 2 / 0
except Exception as e:
    print(e)

try :
    a=3/0
except ZeroDivisionError as e:
    print(e)

# using else with try catch
try:
    b=45/2
except Exception as e:
    print(e)
else:
    print("no exception")
finally:
    print("denominator can't be zero")