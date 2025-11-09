try:
    number_to_generate = int(input("Enter the number to generate: "))
    max_multiplier = int(input("Enter the max multiplier: "))

    for i in range(1, max_multiplier + 1):
        result = number_to_generate * i
        print(f"{number_to_generate} x {i} = {result}")

except ValueError:
    print("Should be an integer")