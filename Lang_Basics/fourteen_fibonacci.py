n = int(input("Enter number of terms: "))

a, b = 0, 1   # first two numbers

print("Fibonacci sequence:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
