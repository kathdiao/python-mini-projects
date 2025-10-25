try:
    grade = int(input("Enter your grade: "))
    if grade < 0 or grade > 100:
        print("Invalid grade")
    elif grade >= 95:
        print("With highest honors")
    elif grade >= 90:
        print("With honors")
    elif grade >= 75:
        print("Pass")
    else:
        print("Fail")
except ValueError:
    print("Invalid value")
