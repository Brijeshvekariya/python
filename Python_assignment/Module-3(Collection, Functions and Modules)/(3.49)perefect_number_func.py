def perfect(n):
    sum = 0
    if n>0:
        for i in range(1,n):
            if n%i == 0:
                sum += i
        if sum == n:
            print(n," is Perfect Number")
        else:
            print(n," is not Perfect Number")    
    else:
        print("Enter Non-Negative Number")

n = int(input("Enter Any Number : "))
perfect(n)