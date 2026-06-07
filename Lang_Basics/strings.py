# using single quote
# name = 'John'

# using double quotes
# name = "John"

# using constructor
# name = str('John')
# print(name)

strng = "Hello World"
print(strng + ' of Worlds')
print(strng * 3)

print(strng[1:-1]) # ello Worl
print(strng[::-1]) # dlroW olleH
print(strng[-5:-2]) # Wor

# Formatting strings
age = 30
sent = f'My name is John, I am {age} years old'
print(sent)

price = 55
sentence = f'The price is ${price:.2f}'
print(sentence)
print(f'The price for two items is ${2 * price:.2f}')

# f string is required when one wants to concatenate string & number otherwise we get type error

sentence1 = 'welcome to Python'
print('come' in sentence1) # True
print('java' not in sentence1) # True