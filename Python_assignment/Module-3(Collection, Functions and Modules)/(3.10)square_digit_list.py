l1 = []
for i in range(0,30):
    l1.append(i+1)
l2 = []
for i in range(0,5):
    l = l1[i] * l1[i]
    l2.append(l)
for i in range(-5,0):
    l = l1[i] * l1[i]
    l2.append(l)
print(l2)
