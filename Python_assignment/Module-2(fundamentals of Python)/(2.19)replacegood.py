string = input("Enter the String : ")
snot = string.find("not")
spoor = string.find("poor")
if snot < spoor and snot>0 and spoor>0:
    string = string.replace(string[snot:], "good")
    print(string)
else:
    print(string)