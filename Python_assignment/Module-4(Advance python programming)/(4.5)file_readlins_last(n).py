n = int(input("Enter Number of lines from last you want to read : "))

with open("(4.4)file3.txt",'r') as file:
    for line in file.readlines()[-n:]:
        print(line)
        