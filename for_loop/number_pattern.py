#Star Pattern
try:
    rows = int(input("Enter number of rows: ? "))
    #outer loop = how many line
    for i in range(1, rows + 1):
        # inner loop = how many items per line
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
except ValueError:
    print("Not a number")


rows1 = 10
for i in range(1, rows1 + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()