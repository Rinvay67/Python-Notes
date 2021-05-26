class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, value):
        if value < 0 or value > 100:
            raise ValueError('Invalid score')
        self.__score = value


s = Student("Bob", 90)
s.set_score(1000)


class Teacher(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value < 0 or value > 100:
            raise ValueError('Invalid score')
        self.__score = value


t = Teacher("Alice", 90)
print(t.score)
t.score = 1000
print(t.score)
