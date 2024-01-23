#defines the std class with attributes std id, name, dob and marks
class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_marks(self, course_id, marks): #add marks for a specific course for a std
        self.marks[course_id] = marks

    def get_marks(self, course_id): #retrieves the marks for a specific course for a std
        return self.marks.get(course_id)

#defines a course class with attributes course id, name
class Course: 
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

#defines school class with attributes std and courses to store list of stds and courses
class School: 
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student): #add std to the list
        self.students.append(student)

    def add_course(self, course): #ad a course to the list
        self.courses.append(course)

    def list_courses(self): #list all the courses in the school, displaying theirs id and name
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Name: {course.name}")

    def list_students(self): #list all the std 
        for student in self.students:
            print(f"Student ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

    def find_student_by_id(self, student_id): #search std in the school based on their id and return the std object if found, or None if not found
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_course_by_id(self, course_id): #search the course in the school based on its id and return the course object if found and none if not found
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None


class UserInterface: #take a school object as an argument and stores it as an attribute
    def __init__(self, school):
        self.school = school

    def input_number_of_students(self): #enter the numb of std and return it as an int
        return int(input("Number of students in the class: "))

    def input_student_information(self): #enter in4 of std(id, name, dob) and create a std object with that in4 and add it to the school
        student_id = input("Std ID: ")
        name = input("Name: ")
        dob = input("Dob: ")
        student = Student(student_id, name, dob)
        self.school.add_student(student)

    def input_number_of_courses(self): #enter the numb of course and return it as an int
        return int(input("Number of courses: "))

    def input_course_information(self): #enter the in4 of course
        course_id = input("Course ID: ")
        name = input("Course name: ")
        course = Course(course_id, name)
        self.school.add_course(course)

    def input_student_marks(self, course_id): #executed if the std is not found based on entered id
        self.school.list_students()
        student_id = input("Std ID: ")
        marks = input("Mark: ")
        student = self.school.find_student_by_id(student_id)
        if student:
            student.add_marks(course_id, marks)
            print("Marks added successfully.")
        else:
            print("Student not found.")

    def select_course(self): #list all the course and select course by entering its id
        self.school.list_courses()
        selected_course = input("Select a course by entering course ID): ")
        return selected_course


/#enter a student ID and retrieves the corresponding student object using find_student_by_id(). 
It then retrieves the marks for the specified course using get_marks(). 
If the student and marks are found, it also retrieves the name of the course using find_course_by_id() and prints the student's ID, name, course name, and marks. 
If the marks are not found or the student is not found, appropriate error messages are displayed.

    def show_student_marks(self, course_id):
        self.school.list_students()
        student_id = input("Std ID: ")
        student = self.school.find_student_by_id(student_id)
        if student:
            marks = student.get_marks(course_id)
            if marks:
                course_name = self.school.find_course_by_id(course_id).name
                print(f"Std ID: {student.student_id}, Name: {student.name}, Course: {course_name}, Marks: {marks}")
            else:
                print("Marks not found.")
        else:
            print("Student not found.")

#the main entry point for the user interface. It prompts the user to input the number of students and their information, as well as the number of courses and their information. 
Then, it allows the user to select a course, input student marks for that course, and display the marks for the selected course and student.
    def run(self):
        num_students = self.input_number_of_students()
        for _ in range(num_students):
            self.input_student_information()

        num_courses = self.input_number_of_courses()
        for _ in range(num_courses):
            self.input_course_information()

        selected_course = self.select_course()
        self.input_student_marks(selected_course)
        self.show_student_marks(selected_course)

#creates a School object and a UserInterface object with the School object as an argument. 
It then calls the run() method of the UserInterface object to start the program execution.
school = School()
interface = UserInterface(school)
interface.run()


#use interface here because:
1. separate the class to make sure when changing sth, it won't be affect the left
2. can reuse and easier collaboration 