# # approach 1
# import class_as_module
# import class_as_module_another
# aobj = class_as_module.Animal()
# bobj = class_as_module_another.Bird()
# aobj.display()
# bobj.display()

# approach 2/3
from class_as_module import *
from class_as_module_another import *
aobj = Animal()
aobj.display()

bobj = Bird()
bobj.display()
