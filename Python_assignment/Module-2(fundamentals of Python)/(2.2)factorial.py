num = int(input("Enter Any Number : "))
fact = 1
for i in range(num,0,-1):
    fact *=i
print("\nThe factorial of %d is "%num,fact)