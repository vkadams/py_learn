# Errors refers to syntax errors or config related errors needs to be
# stops from running the program
# fixed during run time if not done during compile time
'''
Exceptions are not errors and will not stop the program from running.
we need to handle exceptions.
the program will automatically terminate when exception occurs
'''

import os

# exception examples-
# n = 10
# result = n / 0 # throws exception ZeroDivisionError: division by zero
# print(result)

# x = "10"
# print(x + 5) # TypeError: can only concatenate str (not "int") to str

#x = int('welcome') # ValueError: invalid literal for int() with base 10: 'welcome'

# ***  try/except
# print('Start')
# try:
#     print(x)
# except NameError:
#     print("name 'x' is not defined")
# except:
#     print("Some other exception occurred")
# print('End') # the program executes and does not stop


# ***else with try block, else will run when no exception
# try:
#     print('Hello')
# except:
#     print('Something went wrong')
# else:
#     print('Nothing went wrong') # when no exception occured this will run


# ***finally block- will always execute
# try:
#     #print(x)
#     print(os.getcwd())
# except NameError:
#     print('NameError')
# finally:
#     print('finally block')


# ***try except else finally
# try:
#     n = int(input('Enter a value')) # this will always be string
#     result = 100 / n
# except ZeroDivisionError:
#     print('Division by zero, enter number greater than zero')
# except ValueError:
#     print('Invalid input, enter a number')
# else:
#     print('Here is the result',result)
# finally:
#     print('The program will terminate when exception occurs')



# ***try inside try-- nested try
# try:
#     file = open(r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\myfile13.txt','a')
#     try:
#         file.write('Hello World')
#     except:
#         print('Something went wrong when writing data in the file')
#     finally:
#         file.close() # closing the file
# except:
#     print('Something went wrong when opening the file')



# ***custom exceptions--raise exceptions using raise keyword
#eg1
# x = -1
# if x<0:
#     raise Exception('No numbers below zero')

#eg2
# x = 'hello'
# if not type(x) is int:
#     raise TypeError('Only integers are allowed')

#eg3
def set(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    else:
        print('Age set to {}'.format(age))
set(20)
set(-20) # this is where we can use try/except block