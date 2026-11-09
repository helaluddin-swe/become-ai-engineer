
def gradeCalculator(accuracy:float):
    if accuracy>=90:
        return "Expert"
    elif accuracy>=80:
        return "Competent"
    elif accuracy>=70:
        return "Good"
    else:
        return "Needs Improvement"

try:
    inputX=float(input("Enter your marks to check status: "))
    result=gradeCalculator(inputX)
    print(f"status: {result}")

except ValueError:
    print("Enter valid number to check status")