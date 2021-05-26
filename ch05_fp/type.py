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
