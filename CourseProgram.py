"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""

from ast import While
import CourseClass as cc


def main():
    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]

    courseExample = cc.Course(name, crn, seats, status)
    for person in students:
        john = cc.Register(students[0], crn)
        james = cc.Register(students[1], crn)
        Jill = cc.Register(students[2], crn)
        Jack = cc.Register(students[3], crn)
        Joanne = cc.Register(students[4], crn)

    if courseExample.get_seats() > 1:
        print("Student Name: ", john.get_name())
        print("Course Name: ", courseExample.get_name())
        print("CRN: ", courseExample.get_crn())
        courseExample.update_seat_count()
        print("Seats left: ", courseExample.get_seats())
        print()

        print("Student Name: ", james.get_name())
        print("Course Name: ", courseExample.get_name())
        print("CRN: ", courseExample.get_crn())
        courseExample.update_seat_count()
        print("Seats left: ", courseExample.get_seats())
        print()

        print("Student Name: ", Jill.get_name())
        print("Course Name: ", courseExample.get_name())
        print("CRN: ", courseExample.get_crn())
        courseExample.update_seat_count()
        print("Seats left: ", courseExample.get_seats())
        print()

        print("Student Name: ", Jack.get_name())
        print("Course Name: ", courseExample.get_name())
        print("CRN: ", courseExample.get_crn())
        courseExample.update_seat_count()
        print("Seats left: ", courseExample.get_seats())
        print()

    if courseExample.get_seats() == 0:
        print(
            "Sorry ",
            Joanne.get_name(),
            "registration is closed for ",
            courseExample.get_name(),
        )


main()
