# capitalize
print('hello'.capitalize())

print('heLLo'.casefold()) # hello
# similar
print('Hello World'.lower()) # hello world

print('Hello World'.upper())

print('hello world'.title()) # Hello World

print('Hello World'.swapcase()) # hELLO wORLD

# center
print('Hello World'.center(20)) #     Hello World
print('Hello World'.center(20, '*')) # ****Hello World*****

name = 'John'
print('Hello {}'.format(name)) # Hello John

print('Hello'.find('ll')) # 2 - index of first l
print('Hello'.find('x')) # -1

print('Hello'.index('l')) # 2
print('Hello'.index('H')) # 0
print('Hello'.index('o')) # 4
# print('Hello'.index('x')) # ValueError

# count method
print('banana'.count('a')) # 3
print('banana'.index('na')) # 2
print('banana'.count('x')) # 0

#  Replace
print('Hello WOrld'.replace('WOrld', 'There'))

# isalnum -- check if alphanumeric
s = 'abc123'
print(s.isalnum()) # True
s2 = 'abc  123'
print(s2.isalnum())  # False because there is a space


# isalpha
s3 = 'adsfABCDfjoaecnao'
print(s3.isalpha()) # True

# isdecimal
s4 = '99'
print(s4.isdecimal()) # True- decimal is 0-9 string

print(s4.isnumeric()) # True

print(s4.isdigit()) # True


# numbers in string format - isdecimal(), isdigit(), isnumeric()
print('123'.isdecimal()) # True
print('???'.isdecimal()) # False
print('10.5'.isdecimal()) # False


