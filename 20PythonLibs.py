from collections import OrderedDict

ascii_lowercase = ['a', 'b', 'c', 'd', 'e']

di = dict(zip(ascii_lowercase, range(5)))
od = OrderedDict(zip(ascii_lowercase, range(5)))

print(di)
print(od)
