def sum(a):
    print(a+10)

sum(5) # 15

# samething using lambda function
x = lambda a:a+10

print(x(10)) # 20

m = lambda x,y,z:x+y+z # m is like x -- name of lambda function
print(m(10,20,30))
# lambda we can pass n number of parameters, it has to be one single expression
