from abc import ABC, abstractmethod
# people in university are students, faculty or staff


class Person(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []
        self.id = self.generate_id()

    def generate_id(self):
        id_hash = 0
        for char in self.name:
            id_hash += ord(char)
        for char in self.surname:
            id_hash += ord(char)
        return id_hash % 1000000000

    @abstractmethod
    def expertise(self):
        raise NotImplementedError

    def __str__(self):
        return f'{self.surname}, {self.name}\nID: {self.id}\nCourses:\n{self.courses} '


class Student(Person):
    # even without those two lines it would still work, not the case for faculty because it has more variables
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def enroll(self, new_course):
        self.course.append(new_course)

    def expertise(self):
        knowledge = 'Courses Taken: '
        for course in self.courses:
            knowledge += f'{course}, '
        return knowledge


class Faculty(Person):
    def __init__(self, name, surname, position, salary, degrees):
        super().__init__(name, surname)
        self.position = position
        self.salary = salary
        self.degrees = degrees

    def assign_course(self, new_course):
        self.courses.append(new_course)

    def expertise(self):
        knowledge = 'Degrees: '
        for degree in self.degrees:
            knowledge += f'{degree}, '
        knowledge += '\nCourses Taught: '
        for course in self.courses:
            knowledge += f'{course}, '
        return knowledge

    def __str__(self):
        return super().__str__() + f'\nPosition: {self.position}\nSalary: {self.salary}'


class StudentWoInheritance:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []

    def enroll(self, new_course):
        self.course.append(new_course)

    def __str__(self):
        return f'{self.surname}, {self.name}\nCourses:\n{self.courses} '


class FacultyWoInheritance:
    def __init__(self, name, surname, position, salary):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.courses = []

    def assign_course(self, new_course):
        self.courses.append(new_course)


student1 = Student("Sam", "Ellis")
print(student1)
print(student1.id)
print(student1.expertise())

faculty1 = Faculty("John", "Smith", "PI", 60000, ['Bachelor in CS', 'PhD in CS'])
print(faculty1)
print(faculty1.expertise())