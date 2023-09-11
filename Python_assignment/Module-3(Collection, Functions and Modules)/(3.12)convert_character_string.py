n = int(input("Enter Number of Elements : "))
l1 = []
for i in range(0,n):
    chr = input(f"Enter {i+1} element : ")
    l1.append(chr)
string = ''
for i in l1:
    string += i
print("The resultant String is : ",string   )