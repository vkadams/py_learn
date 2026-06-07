# tuples are immutable/cannot change- just like strings
'''
can store heterogenous data & not just homogenous data
ordered - items will be stored in same order they were entered
representation - ()
'''

mytuple = tuple([1,2,3,4,5,6])
print(mytuple) # (1, 2, 3, 4, 5, 6)
print(type(mytuple)) # <class 'tuple'>

tup1 = ('apple', 'banana', 'cherry')
# accessing elements
print(tup1[1]) # banana
print(tup1[-1]) # cherry

tup2 = ('apple', 'banana', 'cherry', 'apple')
print(tup2.count('apple')) # 2
print(tup2[:2]) # ('apple', 'banana')

tup3 = ('apple', 'banana', 'cherry', 'apple', 'kiwi', 'orange', 'mango')
print(tup3[-3:-1]) # ('kiwi', 'orange')

# changing values- can be done indirectly - conver it to list
tup4 = ('apple', 'banana', 'cherry')
lst1 = list(tup4)
print(lst1) # ['apple', 'banana', 'cherry']
lst1[2] = 'orange'
print(lst1) # ['apple', 'banana', 'orange']
# conver list to tuple
tup4 = tuple(lst1)
print(tup4) # ('apple', 'banana', 'orange')

# retrieve data from tupple using for loop
tup5 = ('apple', 'banana', 'cherry', 'apple', 'kiwi', 'orange', 'mango')
for i in tup5:
    print(i)

for i in range(len(tup5)):
    print(tup5[i])

if 'apple' in tup5:
    print('apple' in tup5) # True

if 'hello' not in tup5:
    print('hello' not in tup5) # True

# adding new elements to tuple is not possible-- tuple>list>tuple is workaround

# copying tuple into another tuple
tup6 = tup5
print(tup6) # ('apple', 'banana', 'cherry', 'apple', 'kiwi', 'orange', 'mango')

# cannot remove as its immutable

# joining tuples
tup7 = ('a', 'b', 'c')
tup8 = (1, 2, 3)
tup9 = tup7 + tup8
print(tup9) # ('a', 'b', 'c', 1, 2, 3)



