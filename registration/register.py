name = input("Enter your name: ").strip()
age_input = input("Enter your age: ").strip()
email = input("Enter your email: ").strip()
password = input("Please enter your password: ").strip()
confirm_password = input("Please confirm your password: ").strip()

if age_input.isdigit():
    age = int(age_input)
else:
    age = None

user_info = {
    "name": name,
    "age": age,
    "email": email,
    "password": password,
    "confirm_password": confirm_password
}

if not name:
    print("Name is required")
elif age is None:
    print("Age must be a number")
elif not email:
    print("Email is required")
elif not password:
    print("Password is required")
elif not confirm_password:
    print("Confirm password is required")
elif password != confirm_password:
    print("Passwords do not match")
else:
    print("You are successfully registered!")
    print("User Info:", user_info)
