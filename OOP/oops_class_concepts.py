'''
oops allows programmers to create their own objects that have their own methods & attributes.
'''

class Sample():
    pass

mysample = Sample() # instance of above class whcih does nothing
print(type(mysample)) # <class '__main__.Sample'>

class Dog:
    def __init__(self,breed): # when you create instance of this Dog class,
        # python is going to call init method, it is going to use self in order to
        # represent the instance of object itself.
        self.breed = breed

my_dog = Dog(breed='Lab')
print(type(my_dog))  # <class '__main__.Dog'>
print(my_dog.breed)

# class with objects
class Myclass:
    # refer to functions as method within class
    def myfunc(self):  # self represents class
        pass
    def display(self, name):
        print(name)

# creating objects
mc1 = Myclass()
mc1.myfunc()
mc1.display('Andy')

mc2 = Myclass()
mc2.myfunc()
mc2.display('Dana')
# notice that above methods are access using objects
# what if we want to access methods using class?-- we need static method/s
# if the method is to be remained same then its common- we can make it static

#*************************************************************************************************
#***** instance vs static methods
''' method implementation would not change - this can be made static. if any changes are to be done
we can do it in the class itself
Instance methods are normally accessed thru creating objects of class
'''
class Myclass1:
    def m1(self):
        print('This is instance method')

    @staticmethod
    def m2(args): # no self required
        print('This is static method,',args)

ob = Myclass1()
ob.m1() # invoked using object
ob.m2('Hello') # can be invoked using object as well

Myclass1.m2('Hi There!')
# Myclass1.m1() -- throws type error- missing positional argument & this is not static

#*******************************************************************************************

#variables inside class== class or instance variables
class Myclass2:
    a,b = 10,20 # class or instance variables

    def add(self):
        print(self.a+self.b)

    def mul(self):
        print(self.a*self.b)

obj1 = Myclass2()
obj1.add()
obj1.mul()

#**************************************************************************************

# local/global/class variables
i, j =25, 55
class Myclass3:
    c,d = 200, 400

    def add1(self, x, y):
        print(x + y) # local variables
        print(self.c + self.d) # class variables
        print(i + j) # global variables
obj2 = Myclass3()
obj2.add1(1000, 2000)

# ****************************************************************************************

# all variable names are same
m,n = 100, 200
class Myclass4():
    m, n = 500, 600
    def add1(self, m, n):
        print(m + n) # local variables
        print(self.m + self.n) # class variables
        print(globals()['m'] + globals()['n']) # global variables

obj3 = Myclass4()
obj3.add1(5000, 6000)

# ******************************************************************************
# ********** class with constructor *************
# consturctor is used to initializing data
# consturctor will be automatically invoked when object is created
class Myclass5():
    def __init__(self):
        print('This is a constructor')
    def met1(self):
        print('Hello')
    def met2(self, x, y):
        print(x + y)

obj4 = Myclass5() # at this stage itself constructor is invoked & prints- This is a constructor
obj4.met1()
obj4.met2(20,30)

#*************************
# constructor with parameters
class Myclass6():
    name = 'John'
    def __init__(self, name):
        print(name)
        print(self.name)
obj6 = Myclass6('Dana')

#************************************************************************************

# class with constructor & method
class Employee:
    def __init__(self, ename, eid, sal):
        self.ename = ename
        self.eid = eid
        self.sal = sal
        # above constructor is assigning data to the variables
    def display(self):
        print(self.ename, self.eid, self.sal)

e1 = Employee('Jim', 1001, 5000000)
e1.display()

e2 = Employee('Claire', 1002, 8000000)
e2.display()

