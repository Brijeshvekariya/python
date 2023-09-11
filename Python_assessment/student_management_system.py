# create blank student dictionary i.e. main dictionary
student = {}
# create function to print star-line
def printline():
    print("*"*60)
    print()
    # declare menu variable
menu = """

                                               Role Selection

    Press 1 for Counsellor                  Press 2 for Faculty                  Press 3 for Student

                                        Press Any other key to EXIT                    



        """
# declare counsellor menu
counsellor_menu = """
                       
                         Counsellor Options

        1. Add Student
        2. Remove Student
        3. View All Student
        4. View Specific Student 
        5. Quit               

"""
faculty_menu = '''

                        Faculty Options

        1. Add Marks to Student
        2. Veiw All Student
        3. Quit
'''
student_menu = '''

                    Student Options

        1. Change Details
        2. Veiw Details
        3. Quit

'''
status = True
while status:
    print(menu)
    role = (input("Enter your Role : "))
    if role == '1':
        printline()
        print("Welcome Counsellor\n")
        flag = True
        while flag:
            printline()
            print(counsellor_menu)
            choice = int(input("Enter the choice : "))
            if choice == 1:
                printline()
                n = int(input("Enter number of Subject : "))
                printline()
                # create thrid inner dictionary
                fee = {}
                # create first inner dictionary
                details = {}
                # create second inner dictionary
                sub = {}
                # taking input of all details
                serial = int(input("Enter Serial/Roll Number : "))
                if serial in student:
                    print("This Serial/Roll Number exist in System")
                else:
                    first_name = input("Enter a First Name : ").title()
                    last_name = input("Enter a Last Name : ").title()
                    student_check = True
                    # for i in range(1,len(student)+1): #  --> doubt solved
                    for i in student:
                        if first_name == student[i]['first_name'] and last_name == student[i]['last_name']:
                            printline()
                            print("The First name and Last Name is already exist in the System.")
                            student_check = False
                            break
                    if student_check:
                        mobile = int(input("Enter a Mobile Number : "))
                        # adding input in first inner dictionary
                        details['first_name'] = first_name
                        details['last_name'] = last_name
                        details['mobile'] = mobile
                        for i in range(0,n):
                            subject = input("Enter a Subject : ").title()
                            mark = int(input("Enter Marks : "))
                            fees = int(input("Enter Fees : "))
                            # add data in third inner dictionary
                            fee['marks'] = mark
                            fee['fees'] = fees
                        # third inner dictionry added into second inner dictionary 
                            sub[subject] = fee
                            #second dictionry added in first inner dictionary with subject name
                            details['subject'] = sub
                        faculty = input("Enter Faculty Name : ").title()
                        details['faculty'] = faculty
                        student[serial] = details
                        printline()
                        print("Successfully student added in System")
                        # doubt : i want to check whether first name or last name is already add in system or not.
                        printline()
            elif choice == 2:
                printline()
                serial = int(input("Enter Serial/Roll Number : "))
                first_name = input("Enter a First Name : ").title()
                last_name = input("Enter a Last Name : ").title()
                if serial in student:
                    if first_name == student[serial]['first_name'] and last_name == student[serial]['last_name']:
                        print("We Found one Student in our System.")
                        printline()
                        de = input("Are you sure you want to delete this Student(Y/N) : ").upper()
                        if de == 'Y':
                            student.pop(serial)
                            printline()
                            print("Successfully Student Deleted.")
                    else:
                        print("Enter Valid First Name and Last Name.")
                else:
                    print("Enter Valid Serial/Roll Number.")
                printline()
            elif choice == 3:
                printline()
                print(student)
            elif choice == 4:
                printline()
                serial = int(input("Enter Serial/Roll Number : "))
                if serial in student:
                    print(student[serial])
                else:
                    print("Student Doesn't Exist in the System")
            elif choice == 5:
                flag = False
            else:
                print("Enter Valid Input.")

    elif role == '2':
        fee = {}
        details = {}
        printline()
        faculty = input("Enter Your Name : ").title()
        password = input("Enter Your Password : ")
        printline()
        if password == '123':
            flag = True
            while flag:
                print(faculty_menu)
                choice = int(input("Enter ypur choice : "))
                if choice == 1:
                    printline()
                    serial = int(input("Enter Serial/Roll Number : "))
                    if serial in student:
                        print("\nAs per serial/roll number, one student matched.\n\n")
                        subject = input("Enter a Subject : ").title()
                        if subject in student[serial]['subject']:
                            mark = int(input("Enter Marks : "))
                            student[serial]['subject'][subject]['marks'] = mark
                        else:
                            print("No Student subject Matched in System")
                    else:
                        print("Student Doesn't Existin System")
                elif choice == 2:
                    printline()
                    for i in student:
                        if student[i]['faculty'] == faculty :
                            print(student[i])
                elif choice == 3:
                    flag = False
                else:
                    print("Enter valid Option.")
                printline()
        else:
            print("Enter Valid Password")
            
    elif role == '3':
        printline()
        serial = int(input("Enter Serial/Roll Number : "))
        if serial in student:
            flag = True
            while flag:
                print(student_menu)
                choice = int(input("Enter your Choice : "))
                if choice == 1:
                    first_name = input("Enter a First Name : ").title()
                    last_name = input("Enter a Last Name : ").title()
                    mob = int(input("Enter a Mobile Number : "))
                    student[serial]['first_name'] = first_name
                    student[serial]['last_name'] = last_name
                    student[serial]['mobile'] = mob
                elif choice == 2:
                    print(student[serial])
                elif choice == 3:
                    flag = False
                else:
                    print("Enter Valid Option.")
    else:
        printline()
        status = False
#created by Brijesh