def unique(l1):
    l2 = []
    for i in l1:
        if i not in l2 :
            l2.append(i)
    return l2
n = int(input("Enter Number of Elements : "))
l1 = []
for i in range(0,n):
        stg = input(f"Enter {i+1} element : ")
        l1.append(stg)
print("The Unique list is : ",unique(l1))