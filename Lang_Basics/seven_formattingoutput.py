name, age, salary = 'John', 25, 50000.50
'''
%s -- string
%d -- integer
%r -- float
%g -- binary
'''
print('name: %s   salary: %r   age: %d'%(name, salary, age))


'''
using curly braces
{}
'''
print('Name: {}  Age: {}  Salary: {}'.format(name, age, salary))
print('Name: {0}  Salary: {2}  Age: {1}'.format(name, age, salary))

print('welcome to \npython') # next line

print('welcome \tto python') # tab space