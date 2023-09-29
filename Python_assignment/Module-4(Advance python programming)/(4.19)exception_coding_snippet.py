# (Q) How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets
# ->  Handling exceptions using try, except, and finally blocks in Python is a common practice to gracefully manage errors and ensure that certain cleanup or resource management tasks are performed regardless of whether an exception occurs. 
#     Here are some coding snippets

try:
    a = int(input("Enter any Number : "))
    a = a/0
except (ZeroDivisionError,ValueError):
    print("Error occur")
finally:
    print("Thank you visiting us.")