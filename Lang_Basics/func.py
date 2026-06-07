'''
block of code which only runs when its called.
defined using def keyword
parameter is variable listed inside the parentheses in the func definition
argument is the value that is sent to the func when it is called
method is func if it is created within class & is accessed by creating object of the class
'''

# no parameters & no return value
def myfunc():
    print("hello world from myfunc")

myfunc()

# has parameter & no return value
def myfunc1(name): # name is parameter
    print("hello world from myfunc1,", name)

myfunc1("John") # John is argument

# has parameters & returns value
def cal(a, b):
    return a+b

# storing the return value in some variable
sum = cal(20, 10)
print(sum)

# func returns None
def myfunc2():
    return

print(myfunc2()) # None

def myfunc3():
    i=100

print(myfunc3()) # None

