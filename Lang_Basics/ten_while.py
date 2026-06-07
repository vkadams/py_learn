# while loop executes as long as the condition is true
x = 1 # starting point
while x <= 10: # condition
    if x % 2 == 0: # only even numbers
        print('even num:',x)
    x = x + 1 # increment

y = 1
while y <= 10:
    if y % 2 != 0: print('odd num:',y)
    y = y + 1

# Get a number and calculate the sum of its digits using a while loop. For example, for the number 123, the sum is 1+2+3=6.
num = int(input('Enter a number: '))
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10
print(sum_digits)

# Reverse a Number: Take a number and print its reverse. For example, reversing 1234 gives 4321.
numb = int(input('Enter a number: '))
reverse = 0
while numb > 0:
    digit = numb % 10
    reverse = reverse * 10 + digit
    numb = numb // 10
print(reverse)