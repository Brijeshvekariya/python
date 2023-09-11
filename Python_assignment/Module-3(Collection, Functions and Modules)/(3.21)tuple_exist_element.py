t = ('Hello','World','This','is','Python','Language')
string = input("Enter element : ")
count = 0
for i in t:
    if i == string:
        count += 1
if count>0:
    print("The String is Exist in Tuple")
else:
    print("The String is not Exist in Tuple")

    