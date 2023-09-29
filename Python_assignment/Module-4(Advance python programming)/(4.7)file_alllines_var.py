str = ""
with open("(4.4)file3.txt",'r')as file:
    for line in file.readlines():
        str = str + line
    print(str)