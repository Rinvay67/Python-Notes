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
