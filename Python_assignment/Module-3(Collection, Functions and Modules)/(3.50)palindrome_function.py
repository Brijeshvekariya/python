def palindrome(s):
    s1 = s[::-1]
    if s1 == s:
        print(s," is Palindrome")
    else:
        print(s," is not Palindrome")

s = input("Enter any String : ")
palindrome(s)