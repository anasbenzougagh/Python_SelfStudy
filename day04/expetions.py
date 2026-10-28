# errors are handled the same in Python
'''all exceptions in Python are runtime exceptions'''

try:
    num = 10/0
    print(num)
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
finally:
    print('Finally block')

print('Test Completed')

print('--------------------------------')

tuple1 = (10,20,30,40)
try:
    print(tuple1[2000])
except:
    print('The index number is too large')
else:
    print('The index number is valid')

print('---------------Handling Exceptions-----------------')

try:
    raise FileNotFoundError('No such a file')
except SyntaxError:
    print('It is a syntax error')
except OSError:
    print('It is an operating system error')
except ArithmeticError:
    print('It is an arithmetic error')
else: # not going to run, for exception is handled
    print('No error has ocure')
finally:
    print('Finally block')

print('----------------Throw an exception----------------')
raise LookupError('Invalid entry')
# coming code won't run this code block should be in try block only.
'''
throw: used for manually throwing exception
throws: for exceptions handling (in method signature)
'''

