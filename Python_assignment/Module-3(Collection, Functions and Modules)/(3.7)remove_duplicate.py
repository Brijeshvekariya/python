l1 =[]
n = int(input("Enter Number of Elements : "))
for i in range(0,n):
    stg = input(f"Enter {i+1} element : ")
    l1.append(stg)
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)

print("The Final List is : ",l2)
