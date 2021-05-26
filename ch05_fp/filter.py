def is_odd(x):
    return x % 2 == 1


arr = [1, 4, 6, 7, 9, 12, 17]
print(list(filter(is_odd, arr)))
