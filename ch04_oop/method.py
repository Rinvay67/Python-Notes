import types


class Person(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


p1 = Person('Bob')
print(p1.get_name())


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_score(self):
        return self.__score


p1 = Student('Bob', '90')
print(p1.get_score())
print(p1.get_score)


def fn_get_grades(self):
    if int(self.get_score()) >= 80:
        return 'A'
    if int(self.get_score()) >= 60:
        return 'B'
    return 'C'


# types.MethodType
# 将一个函数变成方法
p1 = Student('Bob', '90')
p1.get_grade = types.MethodType(fn_get_grades, p1)
# print(p1.get_grade())
