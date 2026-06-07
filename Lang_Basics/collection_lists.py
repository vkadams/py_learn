# collection types- list, tuple, set, dictionaries
# store group of data in single variable OR represent group of object using single collection varibale
# similar to array list in Java
'''
lists are ordered & mutable/changeable
represent using []
'''
lst1 = [10,20,30,40,50]
lst2 = ['apple', 'banana', 'cherry']
lst3 = [10, 'Apple', 'A', True]
lst4 = list()
print(lst1)
print(lst2)
print(lst3)
print(lst4) # []

print(lst2[-1]) # cherry --last item

# access multiple values from list
lst5 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(lst5[2:5]) # ['cherry', 'orange', 'kiwi']

# this is revering items
print(lst5[::-1]) # ['mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple']

for i in lst5:
    print(i[::-1])

if 'apple' in lst5:
    print('apple is present') # apple is present

print(len(lst5)) # 7

lst6 = ['apple', 'banana', 'cherry', 'apple', 'kiwi', 'apple']
print(lst6.count('apple')) # 3

# sorting
lst7= ['mango', 'kiwi', 'apple', 'strawberry', 'banana']
print('before sorting:',lst7)
lst7.sort()
print('after sorting:',lst7) # ['apple', 'banana', 'kiwi', 'mango', 'strawberry']

# descending sort
lst7.sort(reverse=True)
print('descending sort:',lst7) # descending sort: ['strawberry', 'mango', 'kiwi', 'banana', 'apple']

# reversing list items
lst8 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
lst8.sort()
print(lst8) # ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
lst8.reverse()
print('Reversed list:',lst8) # Reversed list: ['orange', 'mango', 'kiwi', 'cherry', 'banana', 'apple']

# add items using insert()-- based on index, append()-- puts to last
lst9 = ['apple', 'banana', 'cherry']
lst9.append('orange')
print('appended to last',lst9) # appended to last ['apple', 'banana', 'cherry', 'orange']

lst9.insert(1, 'mango')
print('after insertion', lst9) # after insertion ['apple', 'mango', 'banana', 'cherry', 'orange']

# remove items from list - remove(value), pop(index), del list_name[index]
lst10 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'apple']
lst10.remove('orange')
print('orange removed', lst10) # orange removed ['apple', 'banana', 'cherry', 'kiwi', 'apple']

lst10.pop(-1)
print('after pop', lst10) # after pop ['apple', 'banana', 'cherry', 'kiwi']

del lst10[1]
print('after del', lst10) # after del ['apple', 'cherry', 'kiwi']

del lst10 # lst10 will be deleted- print will throw error
# print(lst10) # NameError: name 'lst10' is not defined

# copy list .copy()
mylist = ['apple', 'banana', 'cherry', 'orange']
mylist2 = mylist.copy()
print(mylist) # ['apple', 'banana', 'cherry', 'orange']
print(mylist2) # ['apple', 'banana', 'cherry', 'orange']

mylist3 = list(mylist) # another wat to copy
print(mylist3) # ['apple', 'banana', 'cherry', 'orange']

# joining the lists using +
l1 = ['a', 'b', 'c', 'd']
l2 = [1, 2, 3, 4]
l3 = l1 + l2
print(l3) # ['a', 'b', 'c', 'd', 1, 2, 3, 4]

# joining the lists using for loop
l3 = ['aa', 'bb', 'cc', 'dd']
l4 = [10, 20, 30, 40]
for i in l4:
    l3.append(i)
print('using loop:', l3) # using loop: ['aa', 'bb', 'cc', 'dd', 10, 20, 30, 40]


# joining the lists using extend() method
l5 = ['a1', 'b1', 'c1', 'd1']
l6 = [11, 21, 31, 41]
l5.extend(l6)
print(l5) # ['a1', 'b1', 'c1', 'd1', 11, 21, 31, 41]
