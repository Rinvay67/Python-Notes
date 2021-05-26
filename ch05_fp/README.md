# 函数式编程

## 1. functional

```python
def add(x, y, f):
    return f(x) + f(y)


from cmath import sqrt  # NOQA
print(add(4, 9, sqrt))
```

## 2. map

```python
def f(x):
    return x * x


print(list(map(f, [-2, 5, -6])))
```

## 3. reduce

```python
def f(x, y):
    return x + y


from functools import reduce  # NOQA
print(reduce(f, [-2, 5, -6], 100))
```

## 4. filter

```python
def is_odd(x):
    return x % 2 == 1


arr = [1, 4, 6, 7, 9, 12, 17]
print(list(filter(is_odd, arr)))
```

## 5. sort

```python
my_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # NOQA


def custom_key(word):
    return [my_alphabet.index(letter) for letter in word]


arr = [36, 5, 12, 9, 21]
print(sorted(arr))
print(sorted(arr, reverse=True))
arr2 = ['jack', 'tomas', 'bob', 'tom']
print(arr2)
arr2.sort(key=custom_key)
print(arr2)
```

## 6. type

```python
def f():
    print('call f() ...')
    return g


def g():
    print('call g() ...')


f()
print(f)
print(type(f))
x = f()
x()
print(x)
print(type(x))
```

```python
def myabs():
    """返回一个函数"""
    return abs


def myabs2(x):
    """返回一个数值"""
    return abs(x)
```

## 7. closure

```python
def calc_sum(lst):
    return sum(lst)


arr = [1, 2, 3, 4]
print(calc_sum(arr))


def calc_sum2(lst):
    """返回内部的函数"""
    def lazy_sum():
        return sum(lst)
    return lazy_sum


arr = [1, 2, 3, 4]
f = calc_sum2(arr)
print(f)
print(type(f))
print('可以实现延迟计算，现在开始执行计算：')
res = f()
print(res)
```

```python
def f(x):
    print('f() ...')

    def g():
        # 防止其他代码调用 g
        print('g() ...')
    return g


# 闭包
# 内层函数引用了外层函数的变量（参数也算变量）
# 然后返回内层函数的情况
# 闭包的特点
# 引用了外层函数的局部变量
# 正确使用闭包
# 确保引用的局部变量在函数返回后不能变
def calc_sum2(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum


def count():
    fs = []
    for i in range(1, 4):
        def h():
            return i * i
        fs.append(h)
    return fs


# 使用闭包请注意：返回函数不要引用任何循环变量或者后续会发生变化的变量
f1, f2, f3 = count()
print(f1())  # 期望是1 实际为9
print(f2())  # 期望是4 实际为9
print(f3())
```

## 8. lambda

```python
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x * x, arr)))


def myabs(x): return -x if x < 0 else x


print(myabs(-2))
print(myabs(9))


def is_not_empty(s): return s and len(s.strip()) > 0


arr = ['test', None, '', ' str', '  ', 'END']
print(list(filter(is_not_empty, arr)))
```
