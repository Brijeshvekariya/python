long = ""
with open("(4.4)file3.txt",'r')as file:
    for line in file:
        words = line.split()
        for word in words:
            if len(word) > len(long):
                long = word
    print("Longest Word in file is : ")
    print(long)  

