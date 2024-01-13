def input_numStudents(args):
    return int(input(f"Enter the number of {args}: "))


def input_infos(args):
    item = {}
    item["ID"] = input(f"Enter {args} ID: ")
    item["Name"] = input(f"Enter {args} Name: ")
    if args == "student":
        item["DoB"] = input("Enter Student's date of birth (YYYY-MM-DD): ")
    return item


def input_mark(student, courses):
    if "marks" not in student:
        student["marks"] = {}
    list_courses(courses)
    course_id = input(f"Enter the course ID for {student['Name']}'s mark: ")
    mark = float(input("Enter the mark for the course: "))
    student["marks"][course_id] = mark


def remove_student_from_course(student, course_id):
    if "marks" in student and course_id in student["marks"]:
        del student["marks"][course_id]
        print(f"Removed {student['Name']}'s mark for course {course_id}.")
    else:
        print(f"{student['Name']} does not have a mark for course {course_id}.")


def list_students(students):
    if not students:
        print("There aren't any students yet")
    else:
        print("Here is the student list: ")
        for i, student in enumerate(students):
            print(f"{i + 1}. {student['ID']} - {student['Name']} - {student['DoB']}")
            if "marks" in student:
                print("Marks (Course Id - Mark): ", end="")
                for course_id, mark in student["marks"].items():
                    print(f"{course_id} - {mark}", end=" ")
                print()


def list_courses(courses):
    if not courses:
        print("There aren't any courses yet")
    else:
        print("Here is the course list: ")
        for i, course in enumerate(courses):
            print(f"{i + 1}. {course['ID']} - {course['Name']}")


def find_student_by_id(students, student_id):
    for student in students:
        if student["ID"] == student_id:
            return student
    return None

def add_more_students(students):
    num_students = input_numStudents("students")
    for _ in range(num_students):
        students.append(input_infos("student"))


def main():
    courses = []
    students = []

    add_more_students(students)

    while True:
        print("""
    0. Quit
    1. Add a course
    2. Add student's mark for a course
    3. List students
    4. List courses
    5. Find the student by ID
    6. Remove student from a course
    7. Add more students
    """)

        option = int(input("Your choice: "))

        if option == 0:
            break
        elif option == 1:
            courses.append(input_infos("course"))
        elif option == 2:
            if not students or not courses:
                print("Please add students and courses first.")
            else:
                list_students(students)
                student_id = input("Enter the student ID: ")
                student = find_student_by_id(students, student_id)
                if student:
                    input_mark(student, courses)
                else:
                    print("Student not found.")
        elif option == 3:
            list_students(students)
        elif option == 4:
            list_courses(courses)
        elif option == 5:
            student_id = input("Enter the student ID: ")
            student = find_student_by_id(students, student_id)
            if student:
                print("Student found:")
                print(f"ID: {student['ID']}, Name: {student['Name']}, Date of Birth: {student['DoB']}")
                if "marks" in student:
                    print("Marks:")
                    for course_id, mark in student["marks"].items():
                        print(f"Course ID: {course_id}, Mark: {mark}")
                else:
                    print("No marks available.")
            else:
                print("Student not found.")
        elif option == 6:
            if not students or not courses:
                print("Please add students and courses first.")
            else:
                list_students(students)
                student_id = input("Enter the student ID: ")
                student = find_student_by_id(students, student_id)
                if student:
                    list_courses(courses)
                    course_id = input("Enter the course ID to remove the student from: ")
                    remove_student_from_course(student, course_id)
                else:
                    print("Student not found.")
        elif option == 7:
            add_more_students(students)
        else:
            print("Invalid input. Please try again!")


if __name__ == "__main__":
    main()
