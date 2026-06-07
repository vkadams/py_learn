# encapsulation is done on variables using __ double underscore -- no private keyword
class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0 # private variable represented by double underscore

    # getter
    def get_marks(self):
        return self.__marks

    # setter
    def set_marks(self, marks):
        if marks <= 100:
            self.__marks = marks
        else:
            print('Invalid marks. Must be between 0 and 100.')

sobj = Student('Jim')
sobj.set_marks(90)
print(sobj.get_marks())