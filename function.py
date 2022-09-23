"""
FUNCTION
-> function are the group of statements that are performs a specific task
-> function help break our program into smaller and modular chunks
-> it avoids repetition and makes the code reusable
"""

def fun():          # defining function
    """this is the doc statement"""     #doc string is used to tell the working of function
    print("hello")

fun()       # calling function


# passing parameters
def funadd(a,b):
    c=a+b
    return c

a=funadd(10,23)
print(a)

# to print the docstring of the function
print(fun.__doc__)

"""
SCOPE AND LIFETIME OF Variable
->scope of a variable is the portion of a program where the variables is recognized
-> parameters and variables defined inside a function are not visible from outside the function
-> the lifetime of a variable is the period throughout which the variables exists in the memory.
    the lifetime of variable inside a function is as long as the function executes, they ae destroyed once we return from the function   
"""

"""
typees of function
built-in function
user defined function 
lamda function
"""

#USER-DEFINED FUNCTION
""" 
types of arguments
default arguments
required arguments
keyword arguments
variable arguments
"""
#default arguements
def fun1(a=10,b=19):
    return a+b

print(fun1())
print(fun1(23))     # in case of default arguments if we pass the single value first argument is assigned that value

# required arguments
def fun2(a,b):
    return a+b

print(fun2(10,20))

# variable arguments
# when we do not know that how many agruments we want to pass we use variable aruments
def fun3(*args):
    result=0
    for x in args:
        result+=x
    return result

print(fun3(1,2,3,4,5,6))

#