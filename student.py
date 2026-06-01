
students = {} 

while True: 
    print("\n1.Add Student")
    print("2.Mark Attendance") 
    print("3.Pay Fees")
    print("4.Show Receipt")
    print("5.Exit")
    
    choice = input("Enter choice: ")

    # Add Student
    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        
        students[roll] = {
            "name": name,
            "attendance": 0,
            "fees": 0
        }
        print("Student Added")

    # Attendance 
    elif choice == "2":
        roll = input("Enter Roll No: ")
        if roll in students:
            students[roll]["attendance"] += 1
            print("Attendance Marked")
        else:
            print("Student not found")

    # Fees
    elif choice == "3":
        roll = input("Enter Roll No: ")
        amount = int(input("Enter Fees Amount: "))
        if roll in students:
            students[roll]["fees"] += amount
            print("Fees Paid")
        else:
            print("Student not found")
            
    # Show Receipt - Ye tumhe likhna hai
    elif choice == "4":
        roll = input("Enter Roll No: ")
        if roll in students:
            print(f"Name: {students[roll]['name']}")
            print(f"Attendance: {students[roll]['attendance']}")
            print(f"Fees Paid: {students[roll]['fees']}")
        else:
            print("Student not found")

    # Exit
    elif choice == "5":
        print("Exiting...")
        break
        
    else:
        print("Invalid choice")