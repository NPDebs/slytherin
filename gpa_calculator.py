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
