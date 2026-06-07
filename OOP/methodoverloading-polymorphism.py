print(len('welcome')) #7

mylist = [1,2,3,4,5]
print(len(mylist)) #5

mytuple = (1,2,3,4,5,6,7)
print(len(mytuple)) #7

mydict = {'id': 123, 'name': 'Jim'}
print(len(mydict))#2

# observe that same function len accepting strings/lists/tuples/dictionaries--
# polymorphism- same func different data
# polymorphism achieved using method overloading -- compile time polymorphism

class Human:
    def say_hello(self, name=None):
        if name is not None:
            print(f'Hello {name}')
        else:
            print('Hello')

h = Human()
h.say_hello('Jim') # Hello Jim
h.say_hello()

#**********************************************
class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a + b + c)

cal = Calculation()
cal.add(1, 3, 4) # 8
cal.add() #0
cal.add(1, 2) #3


