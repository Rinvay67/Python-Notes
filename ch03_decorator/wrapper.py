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
