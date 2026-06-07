if 10 < 20: print('10 is greater than 20')
'''
discount slabs
20% if amount exceeds 10000
10% if amount is between 5-10000
5% if amount is between 1-5000
no discount for < 1000
'''
discount = 0
amount = int(input('Enter amount to calculate discount:'))
if amount > 10000:
    discount = amount * (20/100)
    amount = amount - discount
    print(f'This is what you have to pay {amount}')
elif 5000 < amount <= 10000:
    discount = amount * (10/100)
    amount = amount - discount
    print(f'This is what you have to pay {amount}')
elif 1000 <= amount <= 5000:
    discount = amount * (5/100)
    amount = amount - discount
    print(f'This is what you have to pay {amount}')
elif 0 < amount < 1000:
    print(f'This is what you have to pay {amount}')


a = 200
b = 300
print('a is greater') if a > b else print('b is greater') # ternary operator