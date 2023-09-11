def get_string_chars(string):
    if len(string) >1:
        return string[:2] + string[-2:]
    else:
        return ""
string = input("Enter String : ")
print(get_string_chars(string))