from day03.abstraction2 import Shape, Square, Rectangle
from day03.encapsulation1 import Person

shape: Shape = Square(5)

shape2: Shape = Rectangle(5,4)

def display_area (shape : Shape): # parameter's type is restricted to shape objects Only
    print(f'{shape.name} \' area is {shape.area()}')

display_area(shape)
display_area(shape2)

# person1 = Person ('James',35)
# display_area(person1)