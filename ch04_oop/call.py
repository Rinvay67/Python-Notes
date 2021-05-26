class Person(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def __call__(self, friend):
        print('My name is %s,' % self.__name)
        print('My friend is %s' % friend)


p = Person('Tim', 'male')
p('Bob')
