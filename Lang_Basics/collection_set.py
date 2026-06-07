'''
set allows to store all types of data & is mutable
****set is unordered- items will be stored in random order****
Hence index is not supported as items do not follow order
*****Duplicates are not allowed
representation {}
'''

set1 = {1,2,3,4,5,6,7,8,9}
set2 = {'apple', 'banana', 'cherry'}
set3 = {100, 'A', False}
print(set1) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set2) # {'cherry', 'banana', 'apple'}
print(set3) # {False, 100, 'A'}
set4 = set()
print(set4) # set()

# accessing values in set thru loop as index is not possible as they dont follow order
#****** cannot convert set to list-- duplicacy issue - list allows duplicates

set5 = ('apple', 'banana', 'cherry')
for i in set5:
    print(i)

# searching for value in set
set6 = ('apple', 'banana', 'cherry')
print('apple' in set6) # True

# length of set
print(len(set6)) # 3

# counting is not possible as it does not allow duplicates

# sorting set- the values are unordered so it is not possible

# likewise reversing is also not posible as we can sort it

# add items to set- add() -single item, update()- multiple items
set7 = {'apple', 'banana', 'cherry'}
set7.add('orange')
print(set7) # {'orange', 'cherry', 'banana', 'apple'}
set7.update(['mango', 'grapes']) # should add as list collection
print(set7) # {'banana', 'grapes', 'mango', 'orange', 'apple', 'cherry'}

# duplicates are ignored
set8 = {'apple', 'banana', 'cherry', 'apple'}
print(set8) # {'apple', 'cherry', 'banana'}

# remove items- using remove()
set9 = {'apple', 'banana', 'cherry', 'mango'}
set9.remove('mango')
print(set9) # {'banana', 'apple', 'cherry'}

# remove items- using discard()- doesnt throw error if value doesnt exist otherwise same as remove()
set9.discard('banana')
print(set9) # {'cherry', 'apple'}

# remove items- using pop()
set10 = {'apple', 'banana', 'cherry', 'grapes', 'mango'}
set10.pop()
print(set10) # {'banana', 'cherry', 'grapes', 'mango'}
set10.clear() # removes all values
print(set10) # set() empty set

del set10
# print(set10) # NameError: name 'set10' is not defined.

# copying set
set11 = {'apple', 'banana', 'cherry', 'mango'}
set12 = set11
print(set12) # {'banana', 'mango', 'apple', 'cherry'}

set13 = set11.copy()
print(set13) # {'cherry', 'apple', 'banana', 'mango'}

# joining of sets -union()
set14 = {'apple', 'banana', 'cherry', 'mango'}
set15 = {1,2,3,4}
set16 = set14.union(set15)
print(set16) # {'apple', 'mango', 1, 2, 3, 4, 'cherry', 'banana'}

# joining of sets - | symbol
set17 = set16 | set15
print(set17) # {'mango', 1, 2, 3, 4, 'cherry', 'apple', 'banana'}

# retrieving common values using - intersection
set18 = {'a', 'b', 'c', 30}
set19 = {10, 20, 30, 'a'}
set20 = set18.intersection(set19)
print(set20) # {'a', 30}- only common values

# using & operator for intersection
set21 = {1,2,3,4,'a','b','c'}
set22 = {'a', 'b', 'e', 4,5,6}
set23 = set21 & set22
print(set23) # {4, 'b', 'a'}
