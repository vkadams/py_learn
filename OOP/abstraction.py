# Data abstraction means showing only essential features and hiding the complex internal details
# giving access to functionality but hiding the implementation
# import ABC- Abstract base/parent class thats when it will be abstract class
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod # specifies that it is abstract method
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # next step is we need concrete class to implement these methods
class Car(Vehicle):
    def start(self):
        print("car engine start")

    def stop(self):
        print("car engine stop")

#v = Vehicle() # throws error we Cannot instantiate abstract class 'Vehicle'
# we have to create object of car class
c = Car()
c.start()
c.stop()

# *****python unlike java we can see the implementation too so true abstraction cannot
# be achieved! we can easily click on methods & see the implementation.
'''
lets say we build a product and leased it to someone else to use it, but that someone
can see the implementation details and make a copy of it. create a whole new product 
out of it. thats the problem in python. Java is secured in this way because Java does
not allow to see the implementation details, only functionality will be available.
'''