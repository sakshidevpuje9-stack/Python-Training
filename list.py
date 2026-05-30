''' write a python program to display the name marks and grade of the students using list ,function and for loop'''

from tokenize import Name


student =["maithili","ashwini","sangita","priya","sneha"]
marks =[85,90,78,92,88]

def calculate_grade(marks):

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    else:
        grade= "F"  
    
    print("Name:",student[i])
    print("Marks:",marks)
    print("Grade:",grade)
    print("-----------------------------")

for i in range(len(student)):
    calculate_grade(marks[i])
    

    
      
      