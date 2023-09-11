n = int(input("Enter Number of Elements : "))
l1 = []
for i in range(0,n):
    chr = int(input(f"Enter {i+1} element : "))
    l1.append(chr)
print("*"*40)
print()
print("The Existing List is : ",l1)
t = tuple(l1)
print("The Tuple of List is : ",t)
