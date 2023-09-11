<<<<<<< HEAD
string = input("Enter a string: ")
char_box = {}
for char in string:
    if char in char_box:
        char_box[char] += 1
    else:
        char_box[char] = 1
=======
string = input("Enter a string: ")
char_box = {}
for char in string:
    if char in char_box:
        char_box[char] += 1
    else:
        char_box[char] = 1
>>>>>>> 85cf8c3581af470733b0d951790fa5b4a6043b0f
print("The Count of all Characters is : \n",char_box)