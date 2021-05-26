my_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # NOQA


def custom_key(word):
    return [my_alphabet.index(letter) for letter in word]


arr = [36, 5, 12, 9, 21]
print(sorted(arr))
print(sorted(arr, reverse=True))
arr2 = ['jack', 'tomas', 'bob', 'tom']
print(arr2)
arr2.sort(key=custom_key)
print(arr2)
