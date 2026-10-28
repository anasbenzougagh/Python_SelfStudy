import json

print(':JSON file => read :')
path = 'files/Test.json'

json_file = open(path,'r')
print(type(json_file))

dictionary = json.load(json_file)
print(type(dictionary))
print(dictionary)

for x in dict(dictionary): # cast if you can't call the method
    print(x)

json_file.close()

dictionary['name'] = 'Aaron King'
dictionary['age'] = 45

print(dictionary)

print(':JSON file => write :')

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

json_file = open('files/Test2.json', 'w')

json_object = json.dumps(students,indent=2) # Converting a dictionary object to a Json object
                                            # indent is used to formate text, by default the value of it is 0
print(json_object)
json_file.write(json_object)

print(':JSON file => read :')









