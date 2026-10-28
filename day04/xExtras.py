from functools import reduce

print("______________:Closure:______________")  # function inside a function


def display_message():
    def method():
        print('Hello World')
        print('I Love Python')

    method()
    method()
    method()
    method()


display_message()

print('_________________________')


def display_palindromes(string: list):
    # for s in string:
    #     new_s=''
    #     for i in reversed(range(0, len(str(s)))):
    #         new_s += s[i]

    def is_palindrome(s: str) -> bool:
        return s[::-1].lower() == s

    for s in string:
        if is_palindrome(s):
            print(s)


print(":______________map methods______________:")  # function without a name (identifier)

print(':map (Lambda,Data type):')
nums = [10, 20, 30, 40, 50, 60, 70, 80]

# Nameless function [lambda] returns map
nums = list(map(lambda x: x * 10, nums))

print(nums)

names = ('Java', 'JAVA', 'java', 'ruby', 'swift', 'javaSCRIPT')
names = list(map(lambda s: str(s).upper(), names))
print(names)

dictionary = {'x': 100, 'y': 200, 'z': 300}
# 'y'  ,  t[200]
dictionary = dict(map(lambda t: (t[0], t[1] * 10), dictionary.items()))

print(dictionary)

print(':Filter:')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# nums = [ x for x in nums if x % 5 == 0]
nums = list(filter(lambda n: n % 5 == 0, nums))
print(nums)

'''remove items that starts with j'''
names = [a for a in names if not a.lower().startswith('j')]
print(names)

names = list(filter(lambda s: not str(s).lower().startswith('j'), names))
print(names)

print(':Reduce:')
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# reducing to one single value
print(reduce(lambda x, y: x + y, list1))

list2 = ['Java', 'Python', 'C#', 'Ruby']

print(reduce(lambda x, y: f'{x} {y}', list2))
print(type(reduce(lambda x, y: f'{x} {y}', list2)))
