def divisor(n):
    sum=0
    if n>0:
        for i in range(1,n+1):
            if n%i==0:
                sum+=i
        return sum
    else:
        return "Enter non-zero and non-negative Number"
    
n = int(input("Enter any Number : "))
print("The Sum of all Divisors of",n,'is :',divisor(n))