def map(l1,l2):
    d = {}
    if len(l1) != len(l2):
        print("Both the List must have same lenngth")
    else:
        d = dict(zip(l1,l2))  # ----> We can use zip function to map list into dictionary
       
        # for i in range(len(l1)): ----> Another Method to solve this
        #     dict[l1[i]] = l2[i]
        return d
l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']
print(map(l1,l2))
