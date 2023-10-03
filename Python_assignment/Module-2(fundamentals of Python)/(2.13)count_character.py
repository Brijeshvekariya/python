
string = input("Enter a string: ")
char_box = {}
for char in string:
    if char in char_box:
        char_box[char] += 1
    else:
        char_box[char] = 1

print("The Count of all Characters is : \n",char_box)