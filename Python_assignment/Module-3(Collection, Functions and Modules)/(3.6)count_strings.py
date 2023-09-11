string = []
count = 0
n = int(input("Enter Number of Strings : "))
for i in range(0,n):
    str = input("Enter your String : ")
    string.append(str)
for i in string:
    if len(i) >=2:
        if i[0] == i[-1]:
            # print("yes")
            count+=1
print("The Number of String is : ",count)
