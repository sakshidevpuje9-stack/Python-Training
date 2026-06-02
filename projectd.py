
from secrets import choice


students = [
    {
        "name": "Mohini",
        "fees": 5000,
        "attendance": 92,
        "course": "Computer Engineering",
        "years_of_study": 3
    },

    {
        "name": "Rohini",
        "fees": 4500,
        "attendance": 88,
        "course": "Computer Engineering",
        "years_of_study": 2
    },

    {
        "name": "Purva",
        "fees": 6000,
        "attendance": 95,
        "course": "Computer Engineering",
        "years_of_study": 1
    },
    {
        "name": "Satyarth",
        "fees": 4000,
        "attendance": 70,
        "course": "Computer Engineering",
        "years_of_study": 4
    },
    {
        "name": "Satyarth",
        "fees": 4000,
        "attendance": 70,
        "course": "Computer Engineering",
        "years_of_study": 4
    }
]


# Function for Student Status
def get_student_status(fees, attendance):

    if fees >= 5000 and attendance >= 75:
        return "Active Student"
    
    else:
        return "Inactive Student"


# Search Student Function
def search_student():

    name = input("Enter Student Name: ")

    for student in students:

        if student["name"].lower() == name.lower():

            print("\nLogin Successful")
            print("\n--- Student Details ---")

            print("Name :", student["name"])
            print("Fees :", student["fees"])
            print("Attendance :", student["attendance"], "%")
            print("Course :", student["course"])
            print("Years of Study :", student["years_of_study"])

            print(
                "Status :",
                get_student_status(
                    student["fees"],
                    student["attendance"]
                )
            )

            return

    print("Student Not Found!")


# View All Students
def view_students():

    print("\n===== All Students =====")

    for student in students:

        print("\nName :", student["name"])
        print("Fees :", student["fees"])
        print("Attendance :", student["attendance"], "%")
        print("Course :", student["course"])

         
while True:

    print("\n===== Coaching Class Manager =====")
    print("1. Search Student")
    print("2. View All Students")
    print("3. Exit")

    choice = input("Enter Your Choice")

    if choice == "1":
        search_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Invalid choice")
        break