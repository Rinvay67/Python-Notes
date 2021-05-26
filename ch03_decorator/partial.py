print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))


def int2(x, base=2):
    return int(x, base)


print(int2('10100101'))

import functools  # NOQA
int_2 = functools.partial(int, base=2)
print(int_2('10100101'))
