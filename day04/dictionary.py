print('-------------------Dictionary Manipulation-------------------')
employee1 = {}
'''Add individuals'''
# if it doesn't exist adds it
employee1['name'] = 'James'
# Else updates it
employee1['name'] = 'John'
employee1['age'] = 45
employee1['salary'] = 60_0000

print(employee1)

'''Add bulk'''
employee2 = {
    'name': 'James',
    'age': 21,
    'salary': 80_000,
    'full_time': False
}
print(employee2)

print(':Access element by key:')
print(employee2.get('name'))  # Old school
print(employee2['name'])  # Common use

print(':Update element by key:')
employee2['salary'] += 10000  # Common use
print(employee2)

employee2.update({'age': 40})  # Old school
print(employee2)

# employee2.update({'full_time': True})
employee2['full_time'] = True
print(employee2)

print(':pop():')
employee2.pop('full_time')
print(employee2)

print(':popitem():')
employee2.popitem()  # no args needed
print(employee2)

print(':popitem():')
copy = employee2.copy()
print(copy)
print(employee2 is copy)

print('-------------------Iterating Dictionary-------------------')
employee3 = {
    'name': 'Dean',
    'age': 35,
    'salary': 180_000,
    'full_time': False,
    'job_title': 'Developer',
    'company': 'Apple Inc'
}

print(employee3.keys())
for key in employee3.keys():
    # print(f'{key} : {employee3.get(key)}')
    print(f'{key} : {employee3[key]}')

print(":Get values by iteration:")
values = list(employee3.values())
print(values)

for value in employee3.values():
    print(value)

print(":Dictionary of dictionary:")
for x in employee3.items():  # returns
    print(x)
    print(f'{x[0]}:{x[1]}')  # tuples x = 1 [ index 0 , 1]

students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subjects': ('Math', 'Physics')
    },
    'A02': {
        'name': 'Jean',
        'gender': 'Female',
        'gpa': 3.8,
        'subjects': ('Biology', 'Programing')
    },
    'A03': {
        'name': 'Steve',
        'gender': 'Male',
        'gpa': 4,
        'subjects': ['Chemistry', 'Physics']
    }
}

print(':Updating nested dictionary:')

print(students)
students['A01']['gpa'] = 2.5
print(students)

students['A02']['name'] = 'Daniel'
students['A02']['gender'] = 'Male'

# students['A02'].update({'name':'Daniel','gender','Male'})

print(students)

students['A03']['subjects'][1] = 'Biology'
print(students['A03']['subjects'][1])

print(': Loop printing:')
for x in students.items():
    # print(x)                      # to get dictionaries
    # print(x[1])                   # to get inner dictionary
    #xxxxxxxxxxxxxx print(x['name'])              # to get inner dictionary names
    for y in x:
        print(y)                    # get each pair as tuple

print(': Loop printing 2 (Nested Dictionary):')
for value in students.values():
    print(value)
    for item in value.items():
        print(item)