# approach 1 - getting functions from another file
import operations_modules_concept
operations_modules_concept.add(10, 20)
operations_modules_concept.mul(10, 20)
print(operations_modules_concept.person['age'])

# approach 2 - getting specific functions only
from operations_modules_concept import add, mul
add(1000, 500)
mul(12, 34)

# approach 3 - import all functions & i dont know function names
from operations_modules_concept import *
add(30, 50)
mul(60,2)
print(person['country'])
