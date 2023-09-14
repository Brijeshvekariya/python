def ran():
    n = int(input("Enter any Number : "))
    if n in range(10,20):
        return f"{n} is in range of 10 to 20"
    else:
        return f'{n} is not in range of 10 to 20'

print(ran())