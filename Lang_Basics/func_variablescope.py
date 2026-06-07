'''
variables created outside of func are called global variables
variables created inside of func are called local variables
'''

x=20 # global variable
def myfunc():
    y = 10 # local variable
    print(x) # able to access global variable inside the func
    print(y)

myfunc()
print(x)
# print(y) # NameError: name 'y' is not defined-- this is local to function

print('\n')

a=100 # global variable
def myfunc2():
    a=200
    print(a) # this is local a

myfunc2() # 200-- as x is local to func
print(a) # 100 # global

print('\n')

# updating global variable inside the funciton using global keyword
b = 1010
def myfunc3():
    # update value of global variable inside the function
    global b
    b = 2020
    print(b)

myfunc3() # 2020
print(b) # 2020 -- the globally updated within the function


print('\n')
# declare global variable inside the funciton
def myfunc4():
    global c
    c = 3030
    print(c)

myfunc4() # 3030
print(c) # 3030-- we can create global variable inside of func
