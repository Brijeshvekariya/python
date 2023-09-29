class Circle:
    pi = 3.14

    def area(self):
        self.r = int(input("Enter Radius of Circle: "))
        return self.r * self.r * self.pi

    def perimeter(self):
        self.r = int(input("Enter Radius of Circle: "))
        return 2 * self.pi * self.r

c = Circle()
print("Area of Circle is:", c.area())
print("Perimeter of Circle is:", round(c.perimeter(), 3))  # why round off not done