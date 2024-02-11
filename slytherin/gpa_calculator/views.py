from django.shortcuts import render
from django.http import HttpResponse

# def gpa_calculator(request):
#     return HttpResponse("Hello world!")

'''
GRADE => the letter grade corresponding to one's numerical score (e.g 72 = A).
GP (Grade Point) => the standardised numerical value assigned to the letter grade (e.g., A=5.0, B=4.0).
QP (Quality Points): Represents the product of the Grade Points and the number of credit units for the course.
    QP = Unit * GP

GPA => Grade Point Average: A numeric representation of academic performance.
This is the sum of quality points divided by the total number of credits.
'''

# Define function to calculate the CGPA
def gpa_calculator():
    # Create a dictionary "grade_points" where each letter grade is mapped to its corresponding grade point.
    grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1}

    # Initialise empty lists to store credit units and corresponding letter grades for each course.
    credits = []
    grades = []

    # Prompt user to input the number of courses
    num_courses = int(input("Enter the number of courses: "))

    # A loop that iterates over the range of the number of courses entered by the user.
    # Within the loop, collect the credit unit and grade for each course. Converts the grade to uppercase.
    for i in range(num_courses):
        course_unit = int(input(f"Enter the credit unit for course {i + 1}: "))
        course_grade = input(f"Enter the grade for course {i + 1} (A/B/C/D/E): ").upper()

        # Append credit unit and grade to their respective lists
        credits.append(course_unit)
        grades.append(course_grade)
    
    # Create variables to store the total quality points and total credits.
    total_quality_points = 0
    total_credits = 0

    # Then, iterate through the courses, retrieve the corresponding GP from the "grade_points" dictionary
    # Calculate QP for each course; accumulate the total QPs and credits.
    for i in range(num_courses):
        grade_point = grade_points.get(grades[i], 0)
        quality_points = credits[i] * grade_point
        total_quality_points += quality_points
        total_credits += credits[i]
    
    # Calculate GPA
    if total_credits > 0:
        gpa = total_quality_points / total_credits
        print(f"\nYour GPA is: {gpa:.2f}")
    else:
        print("\nYou didn't enter any courses. Your GPA cannot be calculated.")

# Call the GPA calculator function
gpa_calculator()