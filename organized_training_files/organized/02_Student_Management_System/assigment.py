def hallow_world(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")
    return 
all_students={}
all_courses={}
dayes=("Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday")
dom={1,1,1,1,1,1,1,1,3}
print (dom)
print (dayes,"canot be changed")
def student(action):
    if action=="insert_affter_result":
        try:
            course_list = {}
            name=input("inter name : ")
            age= int(input("inter age : "))
            year=int(input("inter year of education : "))
            Department =input("Enter steering department : ")
            Grades_totel=0
            num=int(input("Enter student number of courses : "))

            for i in range(num):
                course=input(f"Enter course {i+1} : ")
                grade_num= int(input(f"Enter grade for course {course} : "))
                while grade_num<0 or grade_num>100:
                    grade_num= int(input(f"Enter grade for course {course} : "))
                leter=grade_leter(grade_num)
                if course not in all_courses:
                    print(f"Course {course} does not exist. Adding it to the list of courses.")
                    act=input(f"Do you want to add course {course} to the list of courses? (y/n): ")
                    if act.lower() == "y":
                        all_courses[course] = {}
                        course_list[course] = {"grade": leter}
                        Grades_totel+=(Grades_totel+grade_num)/len(course_list)
                        print(f"Course {course} added to the list of courses.")
                    else:
                        print(f"Course {course} not added to the list of courses.")
                else:
                    course_list[course] = {"grade": leter}
            all_students[name]={
                "age": age,
                "year": year,
                "Department": Department,
                "Grades": Grades_totel,
                "Courses": course_list
            }
        except Exception as e:
            print(f"Error occurred while adding student: {e}")
    elif action=="show_all_affter_result":
        return all_students
    elif action=="show_student_affter_result":
        student_name=input("Enter student name: ")
        if student_name in all_students:
            print(f"Student: {student_name}")
            print(f"Age: {all_students[student_name]['age']}")
            print(f"Year: {all_students[student_name]['year']}")
            print(f"Department: {all_students[student_name]['Department']}")
            print(f"Grades: {all_students[student_name]['Grades']}")
            print(f"Grade Letter: {grade_leter(all_students[student_name]['Grades'])}")
        else:
            print("Student not found.")


def grade_leter(grade):
    if grade >= 96:
        return "A+,4.0"
    elif grade >= 92:
        return "A,3.7"
    elif grade >= 88:
        return "A-,3.4"
    elif grade >= 84:
        return "B+,3.2"
    elif grade >= 80:
        return "B,3.0"
    elif grade >= 76:
        return "B-,2.8"
    elif grade >= 72:
        return "C+,2.6"
    elif grade >= 68:
        return "C,2.4"
    elif grade >= 64:
        return "C-,2.2"
    elif grade >= 60:
        return "D+,2"
    elif grade >= 56:
        return "D,1.5"
    elif grade >= 52:
        return "D-,1"
    else:
        return "F,0.0"


def courses(action):

    if action=="insert":
        try:
            course=input("Enter course name : ")
            if course not in all_courses:
                all_courses[course] = {"grade": "N/A", "Prerequisites": "N/A","Instructor": "N/A", "Level": "N/A", "Credits": "N/A"}
                print(f"Course {course} added to the list of courses.")
            else:
                print(f"Course {course} already exists.")
        except Exception as e:
            print(f"Error occurred while adding course: {e}")
    elif action=="show_all_affter_result":
        return all_courses
    elif action=="show_course":
        course=input("Enter course name: ")
        if course in all_courses:
            print(f"Course: {course}")
            print(f"Students enrolled: {all_courses[course]}")
        else:
            print("Course not found.")
    
def show_passed_students():
    passed_students = {name: details for name, details in all_students.items() if details['Grades'] >= 60}
    if passed_students:
        print("Passed Students:")
        for student_name, details in passed_students.items():
            print(f"Student: {student_name}, Details: {details}")
    else:
        print("No students have passed.")
def show_failed_students():
    failed_students = {name: details for name, details in all_students.items() if details['Grades'] < 60}
    if failed_students:
        print("Failed Students:")
        for student_name, details in failed_students.items():
            print(f"Student: {student_name}, Details: {details}")
    else:
        print("No students have failed.")
def show_students_with_grade_letter():
    students_with_grade_letter = {name: (details, grade_leter(details['Grades'])) for name, details in all_students.items()}
    if students_with_grade_letter:
        print("Students with Grade Letter:")
        for student_name, (details, grade) in students_with_grade_letter.items():
            print(f"Student: {student_name}, Details: {details}, Grade Letter: {grade}")
    else:
        print("No students found.")
def show_average_grade():
    if all_students:
        total_grades = sum(details['Grades'] for details in all_students.values())
        average_grade = total_grades / len(all_students)
        print(f"Average Grade of All Students: {average_grade:.2f}")
    else:
        print("No students found.")
def show_highest_grade_student():
    if all_students:
        highest_grade_student = max(all_students.items(), key=lambda x: x[1]['Grades'])
        student_name, details = highest_grade_student
        print(f"Highest Grade Student: {student_name}, Details: {details}")
    else:
        print("No students found.")
def show_lowest_grade_student():
    if all_students:
        lowest_grade_student = min(all_students.items(), key=lambda x: x[1]['Grades'])
        student_name, details = lowest_grade_student
        print(f"Lowest Grade Student: {student_name}, Details: {details}")
    else:
        print("No students found.")
def main():
    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. Show all students")
        print("3. Show student details")
        print("4. Add course")
        print("5. Show all courses")
        print("6. Show course details")
        print("7. Show all passed students")
        print("8. Show all failed students")
        print("9. Show all students with grade letter")
        print("10. hallo world")
        print("12. Show average grade of all students")
        print("13. Show highest grade student")
        print("14. Show lowest grade student")
        print("15. Exit")

        choice = input("Enter your choice (1-15): ")

        if choice == "1":
          student("insert_affter_result")
        elif choice == "2":
            students = student("show_all_affter_result")
            for student_name, details in students.items():
                print(f"Student: {student_name}, Details: {details}")
        elif choice == "3":
            student("show_student_affter_result")
        elif choice == "4":
            courses("insert")
        elif choice == "5":
            courses_item = courses("show_all_affter_result")
            for course_title in courses_item:
                print(f"Course: {course_title}")
        elif choice == "6":
            courses("show_course")
        elif choice == "7":
            show_passed_students()
        elif choice == "8":
            show_failed_students()
        elif choice == "9":
            show_students_with_grade_letter()
        elif choice == "10":
            name = input("Enter your name (or leave blank for 'World'): ")
            hallow_world(name)
        elif choice == "12":
            show_average_grade()
        elif choice == "13":
            show_highest_grade_student()
        elif choice == "14":
            show_lowest_grade_student()
        elif choice == "15":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()