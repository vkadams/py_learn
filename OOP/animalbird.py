# approach 1
# import animal_modules_concepts
# import bird_modules_concepts
#
# animal_modules_concepts.fly()
# bird_modules_concepts.fly()
# animal_modules_concepts.color()
# bird_modules_concepts.color()

# approach 2/3 same
from animal_modules_concepts import *
from bird_modules_concepts import *
fly()
color()
# the above will call functions from latest file in this case bird
# in order to get the desired func, lets call files individually

from animal_modules_concepts import *
fly()
color()

