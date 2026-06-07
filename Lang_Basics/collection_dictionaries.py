# store data in key-value pairs
''' there is not index concept as data is stored as key-value pairs, we can use key to extract value
dictionaries are ordered, mutable
duplicates are not allowed for keys, values can be duplicate
somewhat similar to java hashmap, but dict doesnt accept null
'''

# creating dict
mydict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(mydict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# creating using dict constructor dict()
mydict1 = dict(name='John', age=21, country='USA')
print(mydict1) # {'name': 'John', 'age': 21, 'country': 'USA'}

# a key can have multiple values
dict1 = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'colors':['red', 'green', 'blue']}
print(dict1) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'colors': ['red', 'green', 'blue']}

# accessing items- using key
print(dict1['brand']) # Ford

# accessing items- get method
print(dict1.get('brand')) # Ford

# get items from dict
print(dict1.keys()) # dict_keys(['brand', 'model', 'year', 'colors'])
print(dict1.values()) # dict_values(['Ford', 'Mustang', 1964, ['red', 'green', 'blue']])
print(dict1.items()) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('colors', ['red', 'green', 'blue'])])

# search for a key in dict
if 'model' in dict1:
    print('model' in dict1) # True

# add items into dict
dict1['engine'] = 'v6'
print(dict1)

# updating keys
dict1.update({'engine':'v8'})
dict1.update({'year':'2010'})
print(dict1) # {'brand': 'Ford', 'model': 'Mustang', 'year': '2010', 'colors': ['red', 'green', 'blue'], 'engine': 'v8'}


# removing items from dict using pop
mydict2 = {'brand': 'bose', 'product':'headphones', 'model-type': 'noise-reduction', 'year': 2024}
mydict2.pop('model-type') # key needs to be specified
print(mydict2) # {'brand': 'bose', 'product': 'headphones', 'year': 2024}

# removing items from dict using popitem - removes last item from dict
mydict2.popitem()
print(mydict2) # {'brand': 'bose', 'product': 'headphones'}

# removing items from dict using del keyword- using specific key
del mydict2['brand']
print(mydict2) # {'product': 'headphones'}

# clear method
mydict2.clear()
print(mydict2) # {}-- clears all key/values

# deleting dictionary itself
del mydict2 # dictionary is deleted
# print(mydict2) -- NameError: name 'mydict2' is not defined

# copying the dictionary - using copy()
# dict3 = dict1 will copy references too,so not preferred approach
dict3 = dict1.copy()
print(dict1)
print(dict3)

# copying the dictionary - using dict()
dict4 = dict(dict3)
print(dict4)

# length with dictionary
print(len(dict4))

# looping with dictionary
# capturing all keys
for k in dict4.keys():
    print(k)

# capturing all values
for v in dict4.values():
    print(v)

# alternate to print values
for v in dict4:
    print(dict4[v])

# print all items
for item in dict4.items():
    print(item)

# alternate
for x,y in dict4.items():
    print(x, y)