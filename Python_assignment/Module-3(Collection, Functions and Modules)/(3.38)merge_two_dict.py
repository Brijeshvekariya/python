def merge(dict,dict1):
    for i in dict1.keys():
        dict[i] = dict1[i]
    return dict


dict = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o'}
dict1 = {16:'p',17:'q',18:'r',19:'s'}

dict2 = merge(dict,dict1)
print(dict2)

# another methods:
# dict = dict | dict1
# print(dict)

# print({**dict,**dict1})

# dict2 = dict
# dict2.update(dict1)
# print(dict2)