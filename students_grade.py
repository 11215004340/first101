num_students = int(input("Enter the number of students: "))


i = 1
while i <= num_students:
    total_grade = 0
    num_subjects = int(input(f"Enter the number of subjects for student {i}: "))

    for j in range(1, num_subjects + 1):
        grade = float(input(f"Enter subject {j} grade for student {i}: "))
        total_grade += grade

    average_grade = total_grade / num_subjects
    print(f"Average grade for student {i}: {average_grade:.2f}")
    i +=1
