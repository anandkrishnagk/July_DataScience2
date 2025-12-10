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
