def input_number_of_students():
    return int(input("Numb of students in class: "))

def input_student_information():
    student_id = input("id: ")
    name = input("name: ")
    dob = input("dob: ")
    return (student_id, name, dob)

def input_number_of_courses():
    return int(input("Numb of courses: "))

def input_course_information():
    course_id = input("Course id: ")
    name = input("Course name: ")
    return (course_id, name)

def input_student_marks(students):
    course_id = input("Which course id to input mark: ")
    for student in students:
        marks = float(input(f"Enter marks for {student[1]} in course {course_id}: "))
        student[3][course_id] = marks

def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"Course ID: {course[0]}, Course Name: {course[1]}")

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"Student ID: {student[0]}, Name: {student[1]}, Date of Birth: {student[2]}")

def show_student_marks(students):
    course_id = input("Enter the course ID for which you want to see student marks: ")
    print(f"Student marks for course {course_id}:")
    for student in students:
        if course_id in student[3]:
            print(f"Student ID: {student[0]}, Name: {student[1]}, Marks: {student[3][course_id]}")

def main():
    students = []
    courses = []

    num_students = input_number_of_students()
    for _ in range(num_students):
        student = input_student_information()
        students.append((student[0], student[1], student[2], {}))

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course = input_course_information()
        courses.append((course[0], course[1]))

    choice = "1"
    while choice != "5":
        if choice == "1":
            input_student_marks(students)
        elif choice == "2":
            list_courses(courses)
        elif choice == "3":
            list_students(students)
        elif choice == "4":
            show_student_marks(students)

    

if __name__ == "__main__":
    main()
