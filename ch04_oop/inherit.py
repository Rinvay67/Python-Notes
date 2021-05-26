# 继承
class Person(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.__score = score

    def get_score(self):
        return self.__score


# s1 = Student('Bob', 'Male', '90')
# print(s1.get_name())
# print(s1.get_gender())
# print(s1.get_score())


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.__course = course

    def get_course(self):
        return self.__course


p = Person('Tim', 'Male')
s = Student('Bob', 'Male', '90')
t = Teacher('Alice', 'Female', 'English')
print(isinstance(p, Person))
print(isinstance(p, Student))
print(isinstance(p, Teacher))
print(isinstance(s, Student))
print(isinstance(s, Person))
print(isinstance(t, Teacher))
print(isinstance(t, Person))


s = Student('Bob', 'Male', '90')
print(type(s))
print(dir(s))
print(getattr(s, '_Person__name'))
setattr(s, '_Person__name', 'Adam')
print(s.get_name())
