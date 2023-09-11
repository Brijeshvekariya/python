def longest_word(words_list):
    max_len = 0
    for word in words_list:
        if len(word) > max_len:
            max_len = len(word)
    return max_len
words_string = input("Enter a list of words separated by spaces: ")
words_list = words_string.split()
print("The length of Longest Word is : ",longest_word(words_list))
