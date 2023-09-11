def largest(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f"{num1} is Maximum from three Numbers")
    elif num1>num2 and num1<num3:
        print(f"{num3} is Maximum from three Numbers")
    else :
        if num2>num3:
            print(f"{num2} is Maximum from three Numbers")
        else:
            print(f"{num3} is Maximum from three Numbers")
def smallest(num1,num2,num3):
    if num1<num2 and num1<num3:
        print(f"{num1} is Smallest from three Numbers")
    elif num1<num2 and num1>num3:
        print(f"{num3} is Smallest from three Numbers")
    else :
        if num2<num3:
            print(f"{num2} is Smallest from three Numbers")
        else:
            print(f"{num3} is Smallest from three Numbers")
def sum(num1,num2,num3):
    ans = num1+num2+num3
    print("The Sum is ",ans)

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

largest(num1,num2,num3)
smallest(num1,num2,num3)
sum(num1,num2,num3)