try:
    n = int(input("Enter total Numbers : "))
    for i in range(n):
        a = int(input("Enter Odd Numbers Only: "))
        if a%2==0:
            raise ValueError("Error! Number should be ODD")
except ValueError as var:
    print(var)
    