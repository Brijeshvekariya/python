name = input("Enter Any String : ")
sub = "ing"
sub2 = "ly"
count = 0
for character in name:
    count+=1
if count>=3:
# print("The Occurance of %s in given string is : "%sub,name.count(sub)) this function also can be used
    if sub in name:
        print("-------------------------------\n")
        print("\nIn given string 'ing' is used.\n")
        name = name+sub2
        print("-------------------------------\n")
        print("The Result string is : \n",name)
    else:
        name = name+sub
        print("-------------------------------\n")
        print("The Result string is : \n",name)
else:
    print("-------------------------------\n")
    print("The Result string is : \n",name)
