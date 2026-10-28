import numbers
class Shape:

    def __init__(self):
        self.name = type(self).__name__
        # set the name of the shape based on class
    def area(self) -> numbers:
        pass
        # pass is optional here but used to give empty body to the class to achieve abstraction

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square (Shape):
    def __init__(self,side):
        super().__init__()
        self.side = side

square = Square(5)
print(square)