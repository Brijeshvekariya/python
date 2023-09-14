import math
def volume(r,h):
    volume = math.pi*r*r*h
    return (round(volume,2))

def area(r,h):
    area = (2*math.pi*r*h) + 2*math.pi*r*r
    return (round(area,2))

r = int(input("Enter Radius of Cylinder : "))
h = int(input("Enter Height of Cylinder : "))
print("Surface Volume of Cylinder is : ",volume(r,h))
print()
print("*"*60)
print()
print("Area of Cylinder is : ",area(r,h))   # here we can use % formatting as %.2f