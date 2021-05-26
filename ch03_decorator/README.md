# 装饰器

## 1. f1

```python
def f1(x):
    return x * 2


def new_f1(f):
    """装饰器函数"""
    def fn(x):
        print('call ' + f.__name__ + '()')
        return f(x)
    return fn
```

```python
# g1 为装饰后新函数
g1 = new_f1(f1)
print(g1(5))
```

```python
# f1为装饰后新函数，彻底隐藏f1的原始定义
f1 = new_f1(f1)
print(f1(4))
```

## 2. log

```python
def log1(f):
    def fn(x):
        print('call ' + f.__name__ + '() ...')
        return f(x)
    return fn


@log1
def factorial(n):
    from functools import reduce
    return reduce(lambda x, y: x * y, range(1, n + 1))


# @log1
# def add(a, b):
#     return a + b


print(factorial(6))
# print(add(1, 2))


def log2(f):
    def fn(*args, **kwargs):
        print('call ' + f.__name__ + '() ...')
        return f(*args, **kwargs)
    return fn


@log2
def add2(a, b):
    return a + b


print(add2(1, 2))
```

## 3. debug

```python
def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kwargs):
            print('[%s] %s() ... ' % (prefix, f.__name__))
            return f(*args, **kwargs)
        return wrapper
    return log_decorator


@log('DEBUG')
def test():
    pass


test()
```

## 4. wrapper

```python
def f(x):
    pass


def log1(f):
    def wrapper(*args, **kwargs):
        print('call ...')
        return f(*args, **kwargs)
    return wrapper


def log2(f):
    def wrapper(*args, **kwargs):
        print('call ...')
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper


def log3(f):
    import functools
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print('call ...')
        return f(*args, **kwargs)
    return wrapper


@log1
def f1(x):
    pass


@log2
def f2(x):
    pass


@log3
def f3(x):
    pass


print(f.__name__)
print(f1.__name__)
print(f2.__name__)
print(f3.__name__)
# f
# wrapper
# f2
# f3
```

## 5. partial

```python
print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))
# 12345
# 5349
# 74565


def int2(x, base=2):
    return int(x, base)


print(int2('10100101'))
# 165

import functools  # NOQA
int_2 = functools.partial(int, base=2)
print(int_2('10100101'))
# 165
```

## 6. call

```python
def log(f):
    def fn(*args, **kwargs):
        print('call ' + f.__name__ + '() ...')
        return f(*args, **kwargs)
    return fn


class MyContext(object):
    @log
    def __init__(self, name):
        self.__name = name

    @log
    def __enter__(self):
        return self

    def get_name(self):
        return self.__name

    @log
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exc_type: ', exc_type, ', exc_val: ', exc_val, ', exc_tb:', exc_tb)


with MyContext('test') as f:
    print(f.get_name())
```
