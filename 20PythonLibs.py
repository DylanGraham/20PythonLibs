from collections import OrderedDict, defaultdict, namedtuple

ascii_lowercase = ['a', 'b', 'c', 'd', 'e']

dict01 = dict(zip(ascii_lowercase, range(5)))
od = OrderedDict(zip(ascii_lowercase, range(5)))

print(dict01)
print(od)

dd = defaultdict(list)
print(dd['a'])

nt = namedtuple('nt', 'count enabled colour')
tup = nt(count=6, enabled=False, colour='Green')
print(tup)
