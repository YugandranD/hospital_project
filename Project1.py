import datetime as dt
import random
print("Welcome to the hospital\n")

first_name = input("Enter your first name: ").capitalize()
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ").lower()

if len(first_name) == 1:
    print("Please enter the full first name.")
else:
    pass

age = int(input("Enter your current age: "))
mobile_no = input("Enter your mobile number: ")

if len(mobile_no) != 10:
    print("Please enter a valid mobile number.")
else:
    pass

gender = input("Enter your gender (M for male / F for female / O for others): ").capitalize()

print("Checking all the details are correct......")
print(f"Your name is {first_name} {middle_name} {last_name}\nYour age is {age}\nYour contact number is {mobile_no}\nYour gender is {gender}")

current_date = dt.date.today()

user = {}
op = []

while True:
    choice = input("Patient visit or admit (V/A) or previous menu (P)? ").lower()

    if choice == 'v':
        id = input("Enter your patient id: ")

        if id == 5: 
            print(id)
        else:
            print("Invalid patient id!!")

    elif choice == 'a':
        print("Admit:")
        op_sheet = input("Is OP sheet available (Y/N)? ").lower()

        if op_sheet == 'y':
            op_number = input("Enter your OP number (8 digits): ")

            if len(op_number) != 8:
                print("Invalid OP number format.")
            else :
                print("Admission process for OP number:", op_number)

        elif op_sheet == 'n':
            payment = int(input("Pay ₹10 for admission. Enter 10: "))

            if payment == 10:
                admission_date = input("Enter the admission date (YYYY-MM-DD): ")

                if (admission_date - current_date).days < 3:
                    print("Admission process completed on", admission_date)
                else:
                    print("Admission date should be within 3 days from the current date.")

                op_sheet = ''.join(random.sample('0123456789', 8))   
                print("you can get your op sheet no : ",op_sheet )

                room_number = random.randint(1, 99)
                print("Room number allocated:", room_number)

                user[op_number] = {'name': f"{first_name} {middle_name} {last_name}", 'age': age, 'number': mobile_no}
                op.append(op_number)
            else:
                print("your change is ₹ ",payment - 10)
        else:
            print("Invalid choice for OP sheet availability.")

    elif choice == 'p':
        print("Returning to the previous menu.")
        break

    else:
        print("Invalid choice! Please select 'V' for visit, 'A' for admit, or 'P' for the previous menu.")
        break
