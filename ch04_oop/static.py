class Person(object):
    address = 'Earth'

    def __init__(self, name):
        self.name = name


p1 = Person('Bob')
p2 = Person('Alice')
print(Person.address)
print(p1.address)
print(p2.address)
Person.address = 'China'
print(p1.address)
print(p2.address)
p1.address = 'USA'
print(p1.address)
print(Person.address)
print(p2.address)
