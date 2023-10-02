num1 = int(input("Enter ending Range of Fibanocci Series : "))
a=0
b=1
c=0
print("The Fibanocci Series is : ",a,end=" ")
for i in range(0,num1):
    if a<num1:
        print(b,end=" ")
        c = b + a
        a = b
        b = c
        
