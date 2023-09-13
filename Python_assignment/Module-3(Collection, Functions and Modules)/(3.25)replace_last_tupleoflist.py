# Sample list of tuples
list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

n = int(input("Enter new Number : "))

modified_list_of_tuples = []
for t in list_of_tuples:
    t = (t[:-1] + (n,))
    modified_list_of_tuples.append(t) 
print(modified_list_of_tuples)

