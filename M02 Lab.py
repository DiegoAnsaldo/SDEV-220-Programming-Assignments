# Diego Ansaldo
# M02 Lab.py
# This application takes an input of a students first name, last name, and GPA, and tells them if they have made the deans list or
# the honor roll.

while True:
    lName = input("Enter the student's last name: ")
    if lName == "ZZZ":
        print("Shutting Down")
        break
    fName = input("Enter the student's first name: ")
    studentGPA = float(input("Enter the student's GPA: "))
    if studentGPA >= 3.5:
        print(fName + " " + lName + " has made both the Dean's List and the Honor Roll!")
    elif studentGPA >= 3.25:
        print(fName + " " + lName + " has made the Honor Roll!")
    else:
        print("Sadly, " + fName + " " + lName + " has not made the Dean's List or the Honor Roll.")