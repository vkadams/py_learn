print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] n-1 hence 10 wont be printed
print(list(range(1, 11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(2, 11, 2))) # [2, 4, 6, 8, 10]
print(list(range(10, 0, -1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(range(-10, -5))) # [-10, -9, -8, -7, -6]

st1 = 'Hello'
print(st1[::-1]) # olleH
print('HELLO WORLD!'[::-1]) # !DLROW OLLEH