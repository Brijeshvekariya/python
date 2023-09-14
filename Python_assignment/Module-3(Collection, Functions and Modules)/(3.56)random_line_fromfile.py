import random

path = "(3.1)list.txt"
with open(path,"r") as file:
    lines = file.readlines()
    random_line = random.choice(lines)
    print(random_line)
    print(random_line.strip())