#Write a python program to display the grade of a studnet
student_mark = int(input("Enter your mark (0-100): "))
if student_mark >= 80:
    print("Grade A")
elif student_mark >= 60:
    print("Grade B")
elif student_mark >= 40:
    print("Grade C")
else:
    print("Fail")
