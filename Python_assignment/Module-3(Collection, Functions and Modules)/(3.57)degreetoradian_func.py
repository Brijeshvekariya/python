"""
we can also use global variable as PI = 3.14


"""

import math
pi = 3.1400
def radian(degree):
    return degree * math.pi / 180

degree = int(input("Enter Degree Value : "))
print("The Radian Value is : ",radian(degree))


