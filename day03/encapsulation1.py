class Person:
                            # default assigning is used to skip some args
    def __init__(self, name: str = 'Unknown', age: int = 1):
        # self = this can be use in declare and call in java call only
        self.__name = None  # you can't have empty data in a variable
        self.__age = None
        self.set_name(name)  # called in __init__ constructor
        self.set_age(age)
        # Only one constructor allowed

    def get_name(self):
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}')
            # is to throw exception
        return self.__name

    def set_name(self, name: str):  # name:str will give warning
        if type(name) != str:  # this will give exception
            raise RuntimeError(f'Person name must be String')
        if name == '':
            raise RuntimeError(f'Person name cannot be empty')
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age):
        if age < 0 or age > 150:
            raise RuntimeError(f'Invalid  age {age}')

        self.__age = age

    def __str__(self):
        return f'{type(self).__name__} {str(self.__dict__).replace("_Person__","")}'


person1 = Person()
print(person1.get_name())
print(person1.get_age())

person2 = Person('James')
print(person2.get_name())
print(person2.get_age())

person3 = Person('Hazel',27)
print(person3.get_name())
print(person3.get_age())

print(':Printing objects:')
print(person1)
print(person2)
print(person3)