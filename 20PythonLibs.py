from collections import OrderedDict, defaultdict

ascii_lowercase = ['a', 'b', 'c', 'd', 'e']

dict01 = dict(zip(ascii_lowercase, range(5)))
od = OrderedDict(zip(ascii_lowercase, range(5)))

print(dict01)
print(od)

dd = defaultdict(list)
print(dd['a'])
