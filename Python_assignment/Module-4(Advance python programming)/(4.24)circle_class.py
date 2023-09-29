class Circle:
    pi = 3.14
    r = int(input("Enter Radius of Circle : "))

    def area(self,r):
        return r*r*self.pi
       
    def parimeter(self,r):
        return 2*self.pi*r
    
c = Circle()
print("Area of Circle is : ",c.area(c.r))
print(f"Perimeter of Circle is : {c.parimeter(c.r):.2f}")