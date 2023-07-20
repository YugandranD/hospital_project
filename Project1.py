import datetime as dt
import random
from datetime import datetime

def get_user_details():
    print("Welcome to the hospital\n")

    while True:
        name = input("Enter your name: ")
        if len(name) > 2:
            break
        else:
            print("Please enter a name with more than one character.")

    sliced = name.split()
    first_name = sliced[0]
    middle_name = ""
    last_name = ""
    if len(sliced) > 1:
        if len(sliced) > 2:
            middle_name = sliced[1]
        last_name = sliced[-1]

    if middle_name != "":
        print(f"First name: {first_name}, Middle name: {middle_name}, Last name: {last_name}")
    else:
        print(f"First name: {first_name}, Last name: {last_name}")

    age = int(input("Enter your current age: "))

    while True:
        mobile_no = input("Enter your mobile number: ")
        if len(mobile_no) != 10:
            print("Please enter a valid mobile number.")
        else:
            break

    gender = input("Enter your gender (M for male / F for female / O for others): ").upper()

    print("Checking all the details are correct......")
    print(f"Your name is {first_name} {middle_name} {last_name}\nYour age is {age}\nYour contact number is {mobile_no}\nYour gender is {gender}")
    current_date = dt.date.today()

    user = {}
    op = []

    while True:
        choice = input("Patient visit or admit (V/A) or previous menu (P)? ").lower()

        if choice == 'v':
            id = int(input("Enter your patient id: "))

            if len(str(id)) == 5:
                print("You can visit our hospital now.")
                print("Thank you !")
                break
            else:
                print("Invalid patient id!!")
                continue

        elif choice == 'a':
            print("Admit:")
            op_sheet = input("Is OP sheet available (Y/N)? ").lower()

            if op_sheet == 'y':
                while True:
                    op_number = input("Enter your OP number (8 digits): ")

                    if len(op_number) != 8:
                        print("Invalid OP number!!")
                    else:
                        break
                while True:
                    admission_date_str = input("Enter the admission date (YYYY-MM-DD): ")

                    try:
                        admission_date = datetime.strptime(admission_date_str, "%Y-%m-%d").date()
                        break
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD format.")
                        continue

                if (admission_date - current_date).days < 3:
                    room_number = random.randint(1, 99)
                    print("Room number allocated:", room_number)

                    user[op_number] = {'name': f"{first_name} {middle_name} {last_name}", 'age': age, 'number': mobile_no, 'gender':gender} 
                    print("Admission process completed on", admission_date)
                    print(user)

                    op.append(op_number)
                    print(op)
                    break
                else:
                    print("Admission date should be within 3 days from the current date.")
                    continue

            elif op_sheet == 'n':
                payment = int(input("Pay ₹10 for admission. How much you have: "))

                if payment == 10:
                    while True:
                        admission_date_str = input("Enter the admission date (YYYY-MM-DD): ")

                        try:
                            admission_date = datetime.strptime(admission_date_str, "%Y-%m-%d").date()
                            break
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD format.")
                            continue

                    if (admission_date - current_date).days < 3:
                        op_number = ''.join(random.sample('0123456789', 8))
                        print("You can get your op sheet no:", op_number)
                        op.append(op_number)
                        print(op)

                        room_number = random.randint(1, 99)
                        print("Room number allocated:", room_number)

                        userss = {'name': f"{first_name} {middle_name} {last_name}", 'age': age, 'number': mobile_no}
                        op.append(userss)

                        print("Admission process completed on", admission_date)
                        print(user)
                    else:
                        print("Admission date should be within 3 days from the current date.")
                        continue

                else:
                    print("No problem! Your change is ₹", payment - 10)

                    while True:
                        admission_date_str = input("Enter the admission date (YYYY-MM-DD): ")

                        try:
                            admission_date = datetime.strptime(admission_date_str, "%Y-%m-%d").date()
                            break
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD format.")
                            continue

                    if (admission_date - current_date).days < 3:
                        op_number = ''.join(random.sample('0123456789', 8))
                        print("You can get your op sheet no:", op_number)

                        room_number = random.randint(1, 99)
                        print("Room number allocated:", room_number)

                        users = {'name': f"{first_name} {middle_name} {last_name}", 'age': age, 'number': mobile_no}
                        op.append(users)

                        print("Admission process completed on", admission_date)
                        print(user)
                        break

                    else:
                        print("Admission date should be within 3 days from the current date.")
                        continue
            else:
                print("Invalid choice for OP sheet availability.")

        elif choice == 'p':
            print("Returning to the previous menu.")
            get_user_details()  # Call the function to start from the name input again
            break

        else:
            print("Invalid choice! Please select 'V' for visit, 'A' for admit, or 'P' for the previous menu.")
            continue

get_user_details()

