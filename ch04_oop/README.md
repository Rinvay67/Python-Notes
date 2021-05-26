# 面向对象编程

## 1. class

```python
class Person:
    pass


xiaoming = Person()
xiaoming.name = 'Xiao Ming'
xiaoming.gender = 'Male'
xiaoming.birth = '1990-1-1'
xiaohong = Person()
xiaohong.name = 'Xiao Hong'
xiaohong.school = 'NO.1 High School'
xiaohong.grade = 2
xiaoming.grade = xiaohong.grade + 1
```

## 2. init

```python
class Person(object):
    def __init__(self, name, gender, birth):
        self.name = name
        self.gender = gender
        self.birth = birth


xiaoming = Person('Xiao Ming', 'Male', '1990-1-1')
xiaohong = Person('Xiao Hong', 'Female', '1990-2-3')
print(xiaoming.name)
print(xiaohong.name)
```

## 3. attribute

```python
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
```

```python
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
```

```python
class Student(object):
    __slots__ = ('name', 'gender', 'score')

    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score


s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 90
# s.grade = 'A'
```

## 4. static

```python
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
```

```python
class Person(object):
    count = 0

    @classmethod
    def how_many(cls):
        return cls.count

    def __init__(self, name):
        self.__name = name
        Person.count = Person.count + 1


print(Person.how_many())
p1 = Person('Bob')
print(p1)
p2 = Person('Bob')
print(Person.how_many())
```

## 5. method

```python
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
```

## 6. inherit

```python
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
```

```python
class A(object):
    def __init__(self, a):
        print('init A ...')
        self.__a = a


class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print('init B ...')


class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print('init C ...')


class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print('init D ...')


d = D('d')
print(d)
```

## 7. multiploy

```python
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
```

## 8. call

```python
class Person(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def __call__(self, friend):
        print('My name is %s,' % self.__name)
        print('My friend is %s' % friend)


p = Person('Tim', 'male')
p('Bob')
```
