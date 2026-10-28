print("-----------------------LIST-------------------------")

groceries_list = ['Eggs', 'Milk', 'Rice']
# Add element
print(":Add Element:")
groceries_list.append('Chicken')
#
print(":Add Elements:")
groceries_list.extend(('Beef', 'Oranges', 'Onions'))

print(len(groceries_list))
print(groceries_list)

# here word is string sequence = chars [tuple,list or set should be here instead]
# groceries_list[-2:] = 'Cherry'
# slicing will be used to replace one element if '=' is added
groceries_list[-2] = 'Cherry'
print(groceries_list)

print(":Replacing Elements:")
numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers_list)

numbers_list[2:-2] = [300, 4000, 5, 6000]
print(numbers_list)

print(":Slicing List:")
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

list1 = characters[2:-3]
print(list1)  # ['c', 'd', 'e', 'f']

list2 = characters[:4]
print(list2)  # ['a', 'b', 'c', 'd']

list3 = characters[2:]
print(list3)  # ['c', 'd', 'e', 'f', 'g', 'h', 'i']

print(":Updating With a Bigger Range")

characters[2:5] = ['C', 'D', 'E', 'C', 'D', 'E', 'X', 'Y', 'Z']
# Range will be replaced and extra indexed added, existing elements shifted
print(characters)

print(":List Iteration:")
# iterating through each element
names = ['Conor', 'Steve', 'Hazel', 'Breanna']
for each_element in names:
    print(each_element)

#
print(":Iterating through indexes:")
nums = [10, 20, 30, 40, 50, 60]
for i in range(0, len(nums)):
    # nums[i]/= 5 # gives float
    nums[i] = int(nums[i] / 5)
print(nums)

print(":Iterating through indexes backwards:")
nums = [10, 20, 30, 40, 50, 60]
for i in reversed(range(len(nums))):
    print(nums[i])

print(":Reverse using slicing:")
for x in nums[::-1]:
    print(x)

print(":Reverse using function:")
for x in reversed(nums):
    print(x)

print(":While Loop:")
i = 0
while i < len(nums):
    print(nums[i])
    i += 1  # i++

print(":For Loop with increments:")
for i in range(1, 6):
    i += 2
    print(i)

print("-----------------------List method-------------------------")
nums = [60, 500, 10, 20, 15, 5, 0]

print(":Sort Ascending:")
nums.sort()
print(nums)

print(":Sort Descending:")
nums.sort(reverse=True)
print(nums)

print(":Reverse Method:")
# creates new object and needs to be converted list(...)
list1 = [10, 20, 30, 40]
list1 = list(reversed(list1))
print(list1)

print(":Reverse Method {no need to convert}:")
list1.reverse()
print(list1)

print(":Converting data structure [casting]:")
tuple_elements = ('Java', 'Python', 'C#', 'Ruby')

list_elements = list(tuple_elements)
list_elements[-2] = 'C++'
list_elements.append('Swift')

print(list_elements)

tuple_elements = tuple(list_elements)
print(tuple_elements)

print("-----------------------Memory Allocation-------------------------")
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

print(list1 is list2)  # False: mutable: there is a chance this list will change

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3, 4, 5)

print(tuple1 is tuple2)  # True: immutable: 100% not going to change
print("-----------------------------------------------------------------")
print(":Remove Method:")
groceries_list = ['Eggs', 'Milk', 'Rice']

groceries_list.append('Chicken')
groceries_list.extend(('Beef', 'Oranges', 'Onions'))

print(groceries_list)
groceries_list.remove('Beef')
print(groceries_list)

print(":Remove Method [pop]:")
# pop last item
groceries_list.pop()
print(groceries_list)

# pop by element
groceries_list.pop(1)
print(groceries_list)

print(":Insert Method:")
groceries_list.insert(2, 'Apple')
print(groceries_list)

print(":Index Method:")
print(groceries_list.index('Eggs'))

print(":Count Method:")
nums = [1, 2, 2, 1, 3, 2, 1, 1, 1, 2, 2, 1]
print(nums.count(1))

print("-----------------------Comprehensions-------------------------")
# Remove if in Java
nums = []
for x in range(1, 51):
    nums.append(x)
print(nums)

print(':Long form:')
'''
print(':Divisible by 5:')
divisible_by_5 = []
for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)
print(divisible_by_5)
'''
print(':Short form:')
divisible_by_5 = [x for x in nums if x % 5 == 0]
print(divisible_by_5)

print(':Odd and Even:')
even_numbers = [x for x in nums if x % 2 == 0]
odd_numbers = [x for x in nums if x % 2 != 0]
print(even_numbers)
print(odd_numbers)

print(':Remove:')
# remove java.
names = ['Python','Java','java','javaScript','java','JavA','Ruby']
names =[x for x in names if x.lower() != 'java']
# take each element and turn it to lower case.
print(names)
