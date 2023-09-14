def factorial(n):
    if n>=0:
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact
    else:
        return 'Enter Non-Negative Number'
n = int(input("Enter any Number : "))
print("The Factorial is : ",factorial(n))