list_of_tuples = [(1, 2, 3),(), (4, 5, 6), (7, 8, 9),()]
for i in list_of_tuples:
    if i:
        pass
    else:
        list_of_tuples.remove(i)
print(list_of_tuples)
