def insert_string_in_middle(string1, string2):
    middle_index = len(string1) // 2
    print(middle_index)
    return string1[:middle_index] + string2 + string1[middle_index-1:]
string1 = input("Enter the String : ")
string2 = input("Enter the string to be insert : ")
print(insert_string_in_middle(string1,string2))