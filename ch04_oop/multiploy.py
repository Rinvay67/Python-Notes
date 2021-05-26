class Person(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def say(self):
        return 'i am a Person, my name is %s' % self.get_name()


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.__score = score

    def get_score(self):
        return self.__score

    def say(self):
        return 'i am a Student, my name is %s' % self.get_name()


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.__course = course

    def get_course(self):
        return self.__course

    def say(self):
        return 'i am a Teacher, my name is %s' % self.get_name()


p = Person('Tim', 'Male')
s = Student('Bob', 'Male', '90')
t = Teacher('Alice', 'Female', 'English')
print(p.say())
print(s.say())
print(t.say())
