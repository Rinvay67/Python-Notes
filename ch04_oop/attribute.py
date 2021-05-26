class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'

    @property
    def title(self):
        return self._title


p = Person('Bob')
print(p.name)
print(p.title)
print(p._title)
# print(p.__job)
