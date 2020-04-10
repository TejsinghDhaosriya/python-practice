s = set()
print(type(s))

s.add(1)
s.add(4)
s =s.union({1,3,5,7,})
s.remove(7)
print(s)