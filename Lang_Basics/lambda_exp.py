# lambda expression is also know as ananymous function
# def square(num):
#     return num**2
from Lang_Basics.map_filter import square

square = lambda num: num**2

my_nums = [1,2,3,4,5,6,7,8,9]
print(list(map(square, my_nums)))
#using lambda -- cube
print(list(map(lambda num: num**3, my_nums))) #[1, 8, 27, 64, 125, 216, 343, 512, 729]

# using lambda to check even
print(list(filter(lambda num: num%2==0, my_nums))) # [2, 4, 6, 8]

#reversing the names using map
print(list(map(lambda name: name[::-1], ['Andy', 'Sally', 'Ruby']))) # ['ydnA', 'yllaS', 'ybuR']
