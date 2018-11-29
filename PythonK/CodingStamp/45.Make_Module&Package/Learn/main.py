#Use module.function and variable
from square2 import base, square

print(base)
print(square(10))
print()


#Use module.class
from person import Person

kangster = Person('Kangster', 30, 'Seoul')
print(kangster.greeting(), end='\n\n')


#
import hello

print('main.py __name__ :', __name__)
