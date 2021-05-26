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
