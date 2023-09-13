dict = {1: 'My name is ', 2: 'brijesh', 3: 'my surname is ', 4: 'vekariya', 5: 'i live in ', 6: 'ahmedabad'}


# In Python, We can traverse through a dictionary using various methods to access its keys, values, or key-value pairs

# using for loop to access keys:

for k in dict.keys():
    print("Keys : ",k)

for v in dict.values():
    print("Values: ",v)

item = {k:v for k,v in dict.items()}
print(item)