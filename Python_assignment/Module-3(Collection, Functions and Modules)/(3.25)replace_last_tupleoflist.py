# Sample list of tuples
list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

n = int(input("Enter new Number : "))

modified_list_of_tuples = [(t[:-1] + (n,)) for t in list_of_tuples]
print(modified_list_of_tuples)

