n = int(input("Enter Number of Elements : "))
l1 = []
for i in range(0,n):
    chr = int(input(f"Enter {i+1} element : "))
    l1.append(chr)
    # making largest value of below variables 
smallest = 10000000000000000000000000000000
second = 1000000000000000000000000000000
for i in l1:
    if i<smallest:
        second = smallest
        smallest = i
    elif i < second and i != smallest:
        second = i
print("The Second Smallest Number in given List is : ",second)