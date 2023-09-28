list = []
with open("(4.4)file3.txt",'r')as file:
    for line in file.readlines():
        line.rstrip("\n")
        list.append(line)
    print(list)