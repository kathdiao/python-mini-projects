# Inverted
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


# Inverted Alphabet
rows1 = int(input("Enter number of rows: "))
for i in range(rows1, 0, -1):
    for j in range(1, i + 1):
        # sa ASCII ang A is 65, so 64 + j or 1 = 65 (A)
        print(chr(64 + j), end=" ")
    print()



#Sequential Letters
rows2 = int(input("Enter number of rows: "))

letter_code = 65

for i in range(1, rows2 + 1):
    for j in range(1, i + 1):
        print(chr(letter_code), end=" ")
        letter_code += 1
        if letter_code > 90:
            letter_code = 65
    print()