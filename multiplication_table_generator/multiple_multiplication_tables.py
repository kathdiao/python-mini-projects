try:
    total_tables = int(input("Enter the total number of tables: "))
    max_multiplier = int(input("Enter the max multiplier: "))

    for i in range(1, total_tables + 1):
        print(f"Table of {i}")
        for j in range(1, max_multiplier + 1):
            result = i * j
            print(f"{i} x {j} = {result}")
        print()

except ValueError:
    print("Should be an integer")