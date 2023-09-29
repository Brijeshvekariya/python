count = 0
with open("(4.4)file3.txt",'r') as file:
    for line in file.readlines():
        count += 1
    print("Total Numbers of lines present in file is : ")
    print(count)