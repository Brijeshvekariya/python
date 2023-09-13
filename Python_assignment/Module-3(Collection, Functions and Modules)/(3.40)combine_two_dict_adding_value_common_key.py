d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200,'d':400}

for d in d1:
    if d in d2:
        d2[d] += d1[d]
    else:
        d2[d] = d1[d]

print(d2)