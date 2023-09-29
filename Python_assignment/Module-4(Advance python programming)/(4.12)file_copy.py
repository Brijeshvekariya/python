str = ""
with open("(4.4)file3.txt",'r')as file:
    str = file.read()
    print(str)

with open("(4.12)file.txt",'w') as file:
        file.write(str+"\n")


