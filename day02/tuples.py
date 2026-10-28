print('-----------------------Tuple-----------------------')
days = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday',1,2,3,4,5,6,7,True,False)

print(type(days))
print(len(days))
print(days)

# elements are fixed cannot be changed
# days[0] = 'Java'
# print(days)

# Calling elements based on index
print(days[0])
print(days[-1])

print('-----------------------Slicing-----------------------')
days = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
# Slicing:
# work_days = days[1:-3]
work_days = days[1:4]
print(work_days)

work_days = days[:-2]
print(work_days)

weekend = days[-3:]
print(weekend)

print('-----------------------Comparing-----------------------')
# equal:  tuple == tuple, is: reference to same object

tuple1 = (1,2,3,4)
tuple2 = (1,2,3,4)

print(tuple1 == tuple2)
print(tuple1 is tuple2)

print('-----------------------Merging-----------------------')
tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = tuple1 * 5
print(tuple4)

print('-----------------------Reverse-----------------------')
reversed_tuple1 = days[::-1]
print(reversed_tuple1)

reversed_tuple2 = tuple(reversed(days))
print(reversed_tuple2)

print('-----------------------Tuple Methods-----------------------')
# index
print(days.index('Wednesday'))

# frequency
numbers=(10,10,10,10,10,20,30,40,50,10)
print(numbers.count(10))

print('-----------------------Tuple Iteration-----------------------')
for x in days:
    print(x)

print()

for x in range (0,len(days)):
    print(x)

print()

for x in reversed(range (0,len(days))):
    print(x)

print('-----------------------Multi Dimensional Tuple-----------------------')
nested_tuple = ((1,2,3),(4,5,6),(7,8,9))
print(len(nested_tuple))

print('--------------------------')

for x in nested_tuple:
    print(x)
    for y in x:
        print(y)

print('--------------------------')
for i in range(0,len(nested_tuple)):
    for j in range(0,len(nested_tuple[i])):
        print(nested_tuple[i][j])