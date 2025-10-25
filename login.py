username = 'admin'
password = '1234'

attempts = 3
while attempts > 0:
    input_uname = input("Enter Username: ")
    input_password = input("Enter Password: ")

    if input_uname == username and input_password == password:
        print("Login Successful")
        print(f"Welcome {input_uname}!")
        break
    else:
        if input_uname != username and input_password != password:
            print("Invalid username and password")
            attempts -= 1
            print(f"You have {attempts} attempts left")
        elif input_uname != username:
            print("Invalid username")
            attempts -= 1
            print(f"You have {attempts} attempts left")
        elif input_password != password:
            print("Invalid password")
            attempts -= 1
            print(f"You have {attempts} attempts left")
else:
    print("Access Denied")
