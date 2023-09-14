decimal = [1.6,1.8,2.8,0.9,3.1,4.6,8.9,0.1]

max = min = decimal[0]
for n in decimal:
    if n>max:
        max = n
    if n<min:
        min = n
# max = max(decimal)
# min = min(decimal)

print("Maximum number from given Decimal Number is : ",max)
print("Minimum number from given Decimal Number is : ",min)

