def reverse(string):
    count = 0
    for character in string:
        count+=1
    if count%4==0:
        print("\n\nThe Result string is : ",end=" ")
        for i in range(count,0,-1):
            print(string[i-1],end="")
        # print(string[::-1])
    else:
        print("Please enter string length in multiple of 4.")
string = input("Enter String : ")
reverse(string)