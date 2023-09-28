text = input("Enter the text you want to add in file : ")
with open("(4.3)file2.txt",'a') as file:
    file.write(text + "\n")

with open("(4.3)file2.txt",'r') as file:
    print(file.read())