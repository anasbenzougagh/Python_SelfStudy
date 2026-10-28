class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Employee(Person):
    # if default value in variable before the following must be set too
    def __init__(self, name: str, age: int, job_title: str, company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age)
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')

    # no need for str method, for it was inherited form parent class


class Developer(Employee):
    # If there are no additional extra variables the constructor is called implicitly
    def __init__(self, name: str, age: int, job_title: str = 'Software Developer', company_name: str = 'Unknown',
                 salary: int = 0):
        super().__init__(name, age, job_title, company_name, salary)

    def work(self):
        # super().work()
        print(f'{self.job_title} {self.name} is coding')


class Teacher(Employee):
    def __init__(self, name: str, age: int, job_title: str = 'Teacher', company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age, job_title, company_name, salary)

    def work(self):
        print(f'{self.name} is teaching')


employee1 = Employee('Grace', 29, 'QA', 'Apple Inc')

developer1 = Developer('Dean', 21, 'Python Developer', 'Google Inc', 100_000)

teacher1 = Teacher('Breanna', 45, 'Math Teacher')

print(employee1)
print(developer1)
print(teacher1)

employee1.work()
developer1.work()
teacher1.work()
