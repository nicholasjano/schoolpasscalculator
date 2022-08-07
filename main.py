#######################################################################################################
# In this program, I use Python's Object-Oriented Programming to set up 3 students,
# and check if they passed their grade. A completed exam and a mark above 65 will be a pass.
#
# This program utilizes Classes to easily set up and check the students,
# and type hints to make the code easier to understand and navigate.
#
# Made by Nick Jano
#######################################################################################################

# Imports
from Student import Student
import StudentInfo


# Main executable function
def main():
    # Initializing each student's dictionary
    student1_info: StudentInfo = {
        "name": "Nick",
        "mark": 85.5,
        "exam_completed": True
    }
    student2_info: StudentInfo = {
        "name": "Jim",
        "mark": 44,
        "exam_completed": True
    }
    student3_info: StudentInfo = {
        "name": "Megan",
        "mark": 98,
        "exam_completed": False
    }

    # Main dictionary for all students
    students_info = {
        "1": student1_info,
        "2": student2_info,
        "3": student3_info
    }

    # Initializing the students as objects of the class Student,
    # and determining whether they passed, with a corresponding print statement for each
    for student in students_info:
        student_info = students_info.get(student)
        student = Student(student_info.get("name"), student_info.get("mark"))
        student_pass = student.pass_checker(student_info.get("exam_completed"))
        print(student_pass)


# Start of the executable
if __name__ == "__main__":
    main()

# Way to declare variables with type hints (dict method was used instead):
# student1_name: str = "Nick"
# student1_mark: float = 85
# student1_exam: bool = True
