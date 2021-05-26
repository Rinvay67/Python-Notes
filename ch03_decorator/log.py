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
