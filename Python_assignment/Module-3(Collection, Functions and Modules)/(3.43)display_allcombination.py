data = {1:['a','b'],2:['c','d']}
output=[]

for k in data[1]:
    for i in data[2]:
        output.append(k+i)
        
for i in output:
    print(i)