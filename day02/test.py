# import utility
'''this will import every thing, print statements two
and module's name must be called'''
#result = utility.sum(10,20)
#print(result)

# import individual functions (from: static import in Java)
from utility import sum,calculate,concat
result = sum(10,20)
print(result)

result = calculate(10,'+',200)
print(result)

# without from you'll import the function in utility class
# import can be use anywhere in the class unlike Java

import utility
utility.sum(10,20)
utility.concat("Jave","Python")
utility.calculate(10,'*',30)

print("---------------------------------------------------")
# you can update import name using as keyword
import utility as u
u.sum(1,2)
u.concat("Python", "Java")
u.calculate(10,'/',30)

print("---------------------------------------------------")
# you can update function or method name using as keyword
from utility import  sum as s

print(s(15, 16))

import day01.P05_operators