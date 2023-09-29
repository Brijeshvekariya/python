db = {}
try:
    with open("(4.4)file3.txt",'r')as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in db:
                    db[word] += 1
                else:
                    db[word] = 1
        print(db)
except FileNotFoundError:
    print("(file not found)")