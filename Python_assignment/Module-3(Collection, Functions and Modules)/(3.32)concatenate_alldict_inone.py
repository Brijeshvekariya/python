dict1 = { 1: 'My name is ', 2: 'brijesh',}
dict2 = { 3: 'my surname is ', 4: 'vekariya'}
dict3 = { 5: 'i live in ', 6: 'ahmedabad'}

dict = {}

for d in dict1,dict2,dict3:
    for k,v in d.items():
        dict[k] = v
print(dict)



# for proper format:

# dict = dict1
# dict.update(dict2)
# dict.update(dict3)
# print(dict)