# to use the final keyword
from typing import final

pi: final = 3.14
pi = 3.5 # only warns no exceptions
print(pi)

@final
class Animal:
    pass

class Dog (Animal):
    pass


class Employee:
    @final # final method
    def work(self):     # you can add _final_ before method for readability
        print('working')

class Driver(Employee):
    def work(self): # overriding final method cannot be prohibited, yet a warning will be given
        print('Driving')


class Person:
    def __init__(self, age:int):
        self.__age = age

    @property
    def person_age (self):
        return  self.__age

    @person_age.setter
    def person_age (self, age):
        raise  RuntimeError (f' age is constant, can not be changed')
        # raise an error to make it stop if someone wants to change value line 43

person1 = Person(10)
print(person1.person_age)

# person1.person_age = 110
# print(person1.person_age)

print(person1.person_age)
print(person1.__age)
