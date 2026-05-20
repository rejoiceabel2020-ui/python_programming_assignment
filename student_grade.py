def calculate_grade(score):
    if 70 <= score <= 100:
        return "A", 5
    elif 60 <= score <= 69:
        return "B", 4
    elif 50 <= score <= 59:
        return "C", 3
    elif 45 <= score <= 49:
        return "D", 2
    elif 40 <= score <= 44:
        return "E", 1
    else:
        return "F", 0


courses = []

# Variables for GPA calculation
total_grade_points = 0
total_credit_units = 0

# Ask user for number of courses
num_courses = int(input("Enter number of courses: "))

# Loop through each course
for i in range(num_courses):
    print("\nCourse", i + 1)

    #  input
    course_name = input("Course Name: ")
    score = int(input("Score: "))
    credit_unit = int(input("Credit Unit: "))

    # Get grade and grade point
    grade, grade_point = calculate_grade(score)

    # Calculate grade points for the course
    course_grade_points = grade_point * credit_unit

    # Add to totals
    total_grade_points += course_grade_points
    total_credit_units += credit_unit

    # Store course details in dictionary
    course = {
        "Course": course_name,
        "Score": score,
        "Credit Unit": credit_unit,
        "Grade": grade,
        "Grade Point": grade_point
    }

    # Add dictionary to list
    courses.append(course)

    # Display grade
    print("Grade:", grade)

# Calculate GPA
gpa = total_grade_points / total_credit_units

# Display results
print("\n----- STUDENT GPA SUMMARY -----")

for course in courses:
    print(
        course["Course"],
        "| Score:", course["Score"],
        "| Grade:", course["Grade"],
        "| Credit Unit:", course["Credit Unit"]
    )

print("\nTotal Grade Points =", total_grade_points)
print("Total Credit Units =", total_credit_units)
print("Final GPA =", round(gpa, 2))