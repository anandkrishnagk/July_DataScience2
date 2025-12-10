def student_status(x, y):
    """
    x = total classes
    y = classes attended
    """

    if x <= 0:
        return "Invalid total classes"

    attendance_percentage = (y / x) * 100

    if attendance_percentage >= 75:
        status = "Eligible for exam"
    elif attendance_percentage >= 50:
        status = "Attendance warning"
    else:
        status = "Not eligible for exam"

    return f"Attendance: {attendance_percentage:.2f}% | Status: {status}"


# Example usage
result = student_status(100, 68)
print(result)

def calculate_grade(marks):
    """
    marks = total marks obtained
    """

    if marks < 0 or marks > 100:
        return "Invalid marks"

    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return f"Marks: {marks} | Grade: {grade}"
# Example usage
grade_result = calculate_grade(85)
print(grade_result)

