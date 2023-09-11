t = ('Hello','World','This','is','Python','Language','is')
count = 0
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[j] == t[i]:
            count+=1
            print("Yes, In Given Tuple there is repeated elements : ",t[i])
if count == 0:
    print("There is no repeated elements in Tuple.")
            