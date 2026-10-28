# empty {} will return a set
unique_element = {}
print(type(unique_element))

unique_element = set()
print(type(unique_element))

unique_element.add(10)
unique_element.add(10)
unique_element.add(10)
unique_element.add(20)
unique_element.add(20)
unique_element.add(20)
unique_element.add(30)
unique_element.add(40)

print(unique_element)

# no indexes : error
# print(unique_element[1])

# no indexes : slicing not allowed
# print(unique_element[1:])

print(":Remove method:")
# remove exact element
unique_element.remove(10)
print(unique_element)

print(":Update method:")
# print(help(set.update))
unique_element.update({1,2,3,4,5})
print(unique_element)

print(":Pop method:")
# last item removed
unique_element.pop()
print(unique_element)

# pop returns popped element
n = unique_element.pop()
print(n)

print('----------------pop---------------------')
# pop(): removes the first element from the set
numbers = {10, 20, 30, 40, 50, 60}


print('-------------difference-----------------------')
print(":Difference method:")
# compares two sets
# difference(): compares two sets and returns a new set which contains the items that only exist in first set
s1 = {'Java', 'Python', 'C#'}
s2 = {'Ruby', 'Java', 'C++', 'Swift'}

s3 = s1.difference(s2)
print(s3)

print('----------------------intersection-------------------')

# intersection(): compares two sets and returns a new set which contains the common elements of two sets
set1 = {'Java', 'Python', 'C#'}
set2 = {'C++', 'Ruby', 'Swift', 'Java', 'Python'}

set3 = set1.intersection(set2) # common elements among two sets
print(set3)

print('------------------different_update-------------------')

# different_update(): removes the elements of the first Set that exist in the second Set
a1 = {'Book', 'Pen', 'Apple', 'Cherry', 'Coffee'}
a2 = {'Book', 'Apple', 'Banana', 'Grape', 'TV'}

a3 = a1.difference_update(a2)  # elements not shared between two sets
print(a1)                      # removes elements exists in next set

print('---------------intersection_update----------------------')

# intersection_update(): removes the uncommon elements of first & second sets
b1 = {'Python', 'Java', 'C#', 'Wooden Spoon', 'Ruby', 'Swift'}
b2 = {'Wooden Spoon', 'Python'}

b1.intersection_update(b2)
print(b1)


print('------------------symmetric_difference-------------------')
# symmetric_difference(): Compares two sets and returns a new set which contains all elements except the common once
e1 = {'Apple', 'Banana', 'Cherry'}
e2 = {'Grape', 'Strawberry', 'Banana', 'Mango', 'Lemon', 'Apple'}

e3 = e1.symmetric_difference(e2)
print(e3)
