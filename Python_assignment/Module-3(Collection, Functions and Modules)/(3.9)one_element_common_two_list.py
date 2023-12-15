def check(l1,l2):
    for i in l1:
        if i in l2:
            return  True

l2 = []
l1 =[]
n = int(input("Enter Number of Elements of 1 list : "))
for i in range(0,n):
    stg = input(f"Enter {i+1} element : ")
    l1.append(stg)
print("*"*40)
n = int(input("Enter Number of Elements of 2 list : "))
for i in range(0,n):
    stg = input(f"Enter {i+1} element : ")
    l2.append(stg)        

status = check(l1,l2)
print(status)