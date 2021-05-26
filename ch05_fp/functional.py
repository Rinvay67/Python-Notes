def add(x, y, f):
    return f(x) + f(y)


from cmath import sqrt  # NOQA
print(add(4, 9, sqrt))
