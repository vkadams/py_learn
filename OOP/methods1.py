mylist = [1,2,3]
print(len(mylist))

class Sample:
    pass

# using built in functions such as print/length on user defined objects such
# as this sample class
# using dunder or magic methods
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")

b = Book('Python Rocks', "Jose", 200)

#print(b) # displays string version of Book class- <__main__.Book object at 0x00000126E6ED46E0>
# lets define __str__ method to get string representation in Book class
print(b) # Python Rocks by Jose


#print(len(b)) # TypeError: object of type 'Book' has no len()
# lets define __len__ method in book class
print(len(b)) # 200

# deleting variable from computer memory
del b # this prints out A book object has been deleted


