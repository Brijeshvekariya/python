def area(b1,b2,h):
    area = ((b1+b2)*h)/2
    return area



b1 = int(input("Enter value of one side of two parallel sides : "))
b2 = int(input("Enter value of another side of two parallel sides : "))
h = int(input("Enter Height of Trapezoid : "))
print("Area of Trapezoid is : ",area(b1,b2,h))