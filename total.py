sub1=int(input("Enter the first number: "));
sub2=int(input("Enter the second number: "));
sub3=int(input("Enter the third number: "));
sub4=int(input("Enter the fourth number: "));
sub5=int(input("Enter the fifth number: "));
total=sub1+sub2+sub3+sub4+sub5;
print("The total marks is: ",total);
percentage=(total/5);
print("your total  marks is: ",total);
print("The percentage is: ",percentage);

if percentage >= 75:
    print("You have scored distinction");
elif percentage >= 60:
    print("You have scored first class");
elif percentage >= 45:
    print("You have pass only");
else:
    print("You have failed");