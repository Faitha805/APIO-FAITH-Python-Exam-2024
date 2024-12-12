# 3(i)

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible.")

else:
    print("You are not eligible.")

# 3(ii)

def grade_students():
    students_mark = int(input("Enter the student's mark: "))

    if students_mark == 90 or students_mark > 90:
        print(f"The grade for {students_mark} marks is A.")
    
    elif students_mark >= 80 and students_mark <= 89:
        print(f"The grade for {students_mark} marks is B.")

    elif students_mark >= 70 and students_mark <= 79:
        print(f"The grade for {students_mark} marks is C.")

    elif students_mark >= 60 and students_mark <= 69:
        print(f"The grade for {students_mark} marks is D.")

    else:
        print(f"The grade for {students_mark} marks is F")

grade_students()

# 3(iii)
   # Modifying the grade to handle invalid inputs. 
   # Let the invalid mark be above 100 or below 0

def grade_students():
    students_mark = int(input("Enter the student's mark: "))

    if students_mark >= 90 and students_mark <=100:
        print(f"The grade for {students_mark} marks is A.")
    
    elif students_mark >= 80 and students_mark <= 89:
        print(f"The grade for {students_mark} marks is B.")

    elif students_mark >= 70 and students_mark <= 79:
        print(f"The grade for {students_mark} marks is C.")

    elif students_mark >= 60 and students_mark <= 69:
        print(f"The grade for {students_mark} marks is D.")

    elif students_mark >= 0 and students_mark <= 59:
        print(f"The grade for {students_mark} marks is F")

    else:
        print(f"Invalid Input.")

grade_students()



# 3(v)
# Displaying the grade with a message.

def grade_students():
    students_mark = int(input("Enter the student's mark: "))

    if students_mark >= 90 and students_mark <=100:
        print(f"The grade for {students_mark} marks is A. Excellent.")
    
    elif students_mark >= 80 and students_mark <= 89:
        print(f"The grade for {students_mark} marks is B. Excellent.")

    elif students_mark >= 70 and students_mark <= 79:
        print(f"The grade for {students_mark} marks is C. Good.")

    elif students_mark >= 60 and students_mark <= 69:
        print(f"The grade for {students_mark} marks is D. Satisfactory.")

    elif students_mark >= 0 and students_mark <= 59:
        print(f"The grade for {students_mark} marks is F. Needs Improvement.")

    else:
        print(f"Invalid Input.")

grade_students()



