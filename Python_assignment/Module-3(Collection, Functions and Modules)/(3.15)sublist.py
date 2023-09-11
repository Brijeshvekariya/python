n = int(input("Enter Number of Elements : "))
l1 = []
for i in range(0,n):
    chr = int(input(f"Enter {i+1} element : "))
    l1.append(chr)
n1 = int(input("Enter number of elements of sub-list : "))
sublist = []
for i in range(n1):
    chr = int(input(f"Enter {i+1} element : "))
    sublist.append(chr)
count = 0
for i in sublist:
    if i in l1:
        count += 1
if count == len(sublist):
    print()
    print("Sub-List is Present in the Given List")
else:
    print("Sub-List is not Present in the Given List")
    
