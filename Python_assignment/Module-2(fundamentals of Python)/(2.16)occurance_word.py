string = input("Enter Any string : ")
word = string.split()
word_box = {}
for w in word:
    if w in word_box:
        word_box[w] +=1
    else:
        word_box[w] =1
print(word_box)