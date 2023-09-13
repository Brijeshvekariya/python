list_of_tuples = [(1, 'a'), (4, 'b'), (7, 'c')]
list1 = []
list2 = []
for t in list_of_tuples:
    list1.append(t[0])
    list2.append(t[1])
final_dic = dict(zip(list1,list2))
print(final_dic)