# split()
s1 = 'abc@gmail.com'
lst = s1.split('@')
print(lst) # ['abc', 'gmail.com']
print(lst[0]) # abc
print(lst[1]) # gmail.com
# print(lst[2]) # IndexError: list index out of range

s2 = 'one,two,three,four,five,six'
lst1 =s2.split(',')
print(lst1) #['one', 'two', 'three', 'four', 'five', 'six']

# startswith method
s3 = 'welcome you'
print(s3.startswith('W')) # False
print(s3.endswith('you')) # True

