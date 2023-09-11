stg1 = input("Enter first String : ")
stg2 = input("Enter Second String : ")
print(stg1[0])
s2 = stg1[:2] + stg2[2:]
s1 = stg2[:2] + stg1[2:]
print("The Concatenation of two string is : ",s1+" "+s2)