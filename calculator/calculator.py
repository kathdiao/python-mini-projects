try:
    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter another number: "))
        print("Choose operation:\n1. Add(+)\n2. Subtract(-)\n3. Multiply(x)\n4. Divide(/)")
        operation = input("Enter your choice: ")
        if operation == "1":
            result = num1 + num2
            print(f" {num1} + {num2} = {result}")
            end = input("Do you want to exit? (y/n): ")
            if end == "y":
                break
        elif operation == "2":
            result = num1 - num2
            print(f" {num1} - {num2} = {result}")
            end = input("Do you want to exit? (y/n): ")
            if end == "y":
                break
        elif operation == "3":
            result = num1 * num2
            print(f" {num1} x {num2} = {result}")
            end = input("Do you want to exit? (y/n): ")
            if end == "y":
                break
        elif operation == "4":
            result = num1 / num2
            print(f" {num1} / {num2} = {result:.2f}")
            end = input("Do you want to exit? (y/n): ")
            if end == "y":
                break
            #Yung :.2f sa f-string nagro-round ng number sa 2 decimal places para hindi na magpakita ng sobrang daming decimal digits.
        else:
            print("Invalid operation")
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Number can't be divided by zero")
