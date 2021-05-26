def f(x, y):
    return x + y


from functools import reduce  # NOQA
print(reduce(f, [-2, 5, -6], 100))
