class Rectangle:
    length = int(input("Enter length : "))
    breadth = int(input("Enter Breadth : "))
    def area(self,length,breadth):
        return self.length * self.breadth

r = Rectangle()

print("The Area of Rectangle is : ",r.area(r.length,r.breadth))