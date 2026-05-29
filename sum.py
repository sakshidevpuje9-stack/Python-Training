s1=int (input("Enter the first number: "))
s2=int (input("Enter the second number: "))
s3=int (input("Enter the third number: "))
sum=s1+s2+s3
print("The sum of the three numbers is: ",sum)
percentage=(sum/300)*100
print("The percentage is: ",percentage)
if percentage>=90:
    print("Grade: A")
elif percentage>=80:
    print("Grade: B")
elif percentage>=70:
    print("Grade: C")
elif percentage>=60:
    print("Grade: D")
else:
    print("Grade: F")

