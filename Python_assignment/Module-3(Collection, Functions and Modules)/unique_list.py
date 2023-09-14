l1 = [1,2,3,4,5,6,1,2]
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)

print("The Unique List is : ",l2)