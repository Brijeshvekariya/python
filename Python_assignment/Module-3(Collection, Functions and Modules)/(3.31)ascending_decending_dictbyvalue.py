d = {2:'brijesh', 4: 'vekariya',6: 'ahmedabad',1: 'My name is ', 3: 'my surname is ', 5 : 'i live in '}

# Sorting in Ascending order
asc_d = dict(sorted(d.items()))
print(asc_d)
for v in asc_d.values():
    print(v,end=" ")

print()

# Sorting in Descending order
asc_d = dict(sorted(d.items(),reverse=True))
print(asc_d)
for v in asc_d.values():
    print(v,end=" ")
