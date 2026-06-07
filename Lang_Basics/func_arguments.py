# 1 Arbitrary or variable-length arguments
# 2 Positional or required arguments
# 3 Keyword arguments

# 1 Arbitrary or variable-length arguments
def sum_function(*numbers): # all arguments will be stored as tuples
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_function(10, 20))
print(sum_function(10, 20, 30))
print(sum_function(100, 200, 300, 400, 500, 600))
print(sum_function()) # 0

# 2 Positional or required arguments & keyword arguments
def fun1(i , j):
    print(i, j)

fun1(1, 2)
# 1 is assigned to i & 2 is assigned to 2, that refers to positioning

# in case of keyword argument, we can swap positions
fun1(j=50, i=100) # 100 50

# default values to positional arguments
def f1(i=10, j=100):
    print(i, j)

f1(20) # 20 100
f1()

# mixing keyword & positional arguments
def f2(i=100, j=500, k=1000):
    print(i, j, k)

f2(k=2, j=5) # 10 5 2
#**** positional argument must be entered before keyword argument
f2(20,22,k=12)
f2(1000)

# function can return multiple values
def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a

print(largest(300, 400)) # returns tuple (400, 300)

# *args & *kwargs
# return 5% of sum of a & b
def five_Perc_ab(a,b):
    return sum((a,b))*0.05
print(five_Perc_ab(10,20)) # 1.5

# working with more numbers-
def f10(*args):
    return sum(args)*0.1
print(f10(10,20,30,40,50)) # 15.0

#*kwargs- keyword arguments
def f11(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('My fruit of choice is unavailable')

f11(fruit='apple', veggie='lettuce') # My fruit of choice is apple

# args & kwargs
def func15(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food'])) # I would like 10 eggs

func15(10,20,30,fruit='orange',food='eggs',animal='dog')


