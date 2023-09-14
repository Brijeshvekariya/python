# Sample list of tuples
list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

n = int(input("Enter new Number : "))

# modified_list_of_tuples = []
# for t in list_of_tuples:
#     t = (t[:-1] + (n,))
#     modified_list_of_tuples.append(t) 
# print(modified_list_of_tuples)



l = []
for t in list_of_tuples:
    l1 = list(t)
    list_of_tuples.pop(0)
    list_of_tuples.append(l1)
    print(list_of_tuples)
# tup = []
for i in list_of_tuples:
    i[-1] = n
    print(i)
for i in list_of_tuples:
    t = tuple(i)
    list_of_tuples.pop(0)
    list_of_tuples.append(t)
print(list_of_tuples)



