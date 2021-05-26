arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x * x, arr)))


def myabs(x): return -x if x < 0 else x


print(myabs(-2))
print(myabs(9))


def is_not_empty(s): return s and len(s.strip()) > 0


arr = ['test', None, '', ' str', '  ', 'END']
print(list(filter(is_not_empty, arr)))
