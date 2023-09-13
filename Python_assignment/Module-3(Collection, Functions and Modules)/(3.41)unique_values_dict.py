d1 = {'a': 100, 'b': 200, 'c':300,'d': 300, 'e': 200,'f':400}

l = []

for v in d1.values():
    if v not in l:
        l.append(v)

print(l)
