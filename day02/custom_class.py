import numbers


class Employee:

    # static variable of java [to declare you put in class level]

    # is_human = True
    # planet = 'Earth'

    # arg will be passed :[] if the object params weren't declare
    # 4 overloaded constructors
    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')

    def __str__(self):
        return f'{type(self).__name__} {self.__dict__}'
                #getClassName

employee1 = Employee()

print(employee1.name)
print(employee1.job_title)
print(employee1.salary)
print()

employee2 = Employee('John')

print(employee2.name)
print(employee2.job_title)
print(employee2.salary)
print()

employee3 = Employee('Amal', 'Qa')

print(employee3.name)
print(employee3.job_title)
print(employee3.salary)
print()

employee4 = Employee('Yulia', 'Dev', 150_000)

print(employee4.name)
print(employee4.job_title)
print(employee4.salary)
print()

# print(Employee.is_human)
# print(Employee.planet)

employee1.work()
employee2.work()
employee3.work()
employee4.work()

print(employee1)
print(employee2)
print(employee3)
print(employee4)