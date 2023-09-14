'''
To set the starting value in generating random number :

we use random.seed function, this function is used to initialize the pseudo-random number generator with a given seed value. 
By setting the seed value, we can generate the same starting sequence of random numbers every time you run the program

'''

import random

random.seed(15)
random = random.randint(10,20)
print("Random number is : ",random,)
