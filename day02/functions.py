'''
Java Methods:

'''
import numbers


# Non-return value function
def display_message():
    print('hello Cydeo')
    print('hello world')


display_message()


# Return value function
def value():
    return 'Python Programming'


print(value().upper())


def return_int() -> int:
    return 10


print(return_int())


# Accepts all data type dynamic typing
# def square (num):
#     return num * num
# print(square(5))

# Accepts int type only
def square(num: int):
    return num * num


print(square(5))


# print(square('Java'))

def divide(num1, num2):
    return num1 / num2


print(divide(10, 2))


# print(divide('C#', 'Python'))

def add(num1: int, num2: int):
    return num1 + num2


def add2(num1, num2) -> int:
    return num1 + num2


add(10, 20)
add(10.5, 20.5)

print("---------------------------------------------------------------------------")


def calculate(num1: numbers, operator: str, num2: numbers) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print("Invalid Operator")
        return 0


print(calculate(15, '+', 15))

print(calculate(100.5, '/', 2.5))

print("-----------------------Example of method overloading----------------------")


# 4 arg must be given to use the function
# def sum(n1:numbers, n2:numbers, n3:numbers, n4:numbers) ->numbers:

# default arg must be given and assigned if needed
def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    return n1 + n2 + n3 + n4


print(sum(10, 20))
print(sum(10, 20, 30))
print(sum(10, 20, 30, 40))

print(':Method:')
class test:
    # Method needs class
    def method(self):
        pass

print("----------------------------------------------------------------------------")

print(':Function Overloading:')
def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}'.strip())

concat('Cydeo','School')
concat('Python',3,2.5)
concat('Python',3,2.5,True)
concat('Python',3,2.5,True,False)

# There are lots of functions in Python support library creating functions is rare

'''
Functions rules:
1. Declaring
2. Parameters
3. Restricting parameter's data type {arg:str} and return type {()-> str:}
4. Setting default value to parameter int=0 , arg =''

Dynamic Typing
'''
