# strings are immutable
s1 = 'hello'
print('Original string:', s1)
print('Address', id(s1)) # 1848307962752

# **** THis throws as strings are immutable
# s1[0] = 'H' # TypeError: 'str' object does not support item assignment
s1 = 'H'+s1[1:] # this created another object
print(s1)
print('Address after', id(s1)) # 1848307963616 -- the id is different

s2 = 'python'
print(s2)
print('Address before', id(s2))
s2 = s2.replace('p', 'P')
print(s2)
print('Address after', id(s2))

# mutable
lst = ['h', 'e', 'l', 'l', 'o']
print('Original list:',lst)
print('Address before', id(lst)) # 2388862619584
lst[0] = 'H'
print('After change',lst)
print('Address after', id(lst)) # 2388862619584
# same memory location

# ** in case of strings the memory location will be different. so it is immutable
