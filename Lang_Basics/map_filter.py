my_nums=[1,2,3,4,5,6]

def square(num):
    return num**2

# if i want to use this square function for all nums in my_nums, i would use for loop
# lets use map function
for item in map(square,my_nums): # since map is executing, we are not mentioning square(), just square
    print(item)

# check if the entered string is even
def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names))) # ['EVEN', 'E', 'S']

#****filter
def check_even(num):
    return num%2==0
mynums = [1,2,3,4,5,6,7,8,9]
print(list(filter(check_even, mynums))) # [2, 4, 6, 8]