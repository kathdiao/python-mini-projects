print("1. Add note"
      "\n2. View notes"
      "\n3. Delete note"
      "\n4. Exit")

while True:
    user = input("Enter your choice: ")

    if user == "1":
        user_note = input("Enter note: ")

        f = open("notes.txt", "a")
        f.write(f"{user_note}\n")

        print("Note added")

    elif user == "2":
        print("No notes added")
        print("\n--- NOTES ---")
        with open("notes.txt", "r") as f:
            for num, line in enumerate(f, start=1):
                print(f"Day {num}: {line.strip()}")
        print("--------------\n")

    elif user == "3":
        with open("notes.txt", "r") as f:
            notes = f.readlines()

        if not notes:
            print("No notes to delete.")
            continue

        print("\n--- NOTES ---")
        for num, line in enumerate(notes, start=1):
            print(f"Day {num}: {line.strip()}")
        print("--------------")

        try:
            delete_num = int(input("Enter Day number to delete: "))

            if delete_num < 1 or delete_num > len(notes):
                print("Invalid number!")
                continue

            deleted_note = notes.pop(delete_num - 1)

            with open("notes.txt", "w") as f:
                for line in notes:
                    f.write(line)

            print(f"Deleted Day {delete_num}: {deleted_note.strip()}\n")
        except ValueError:
            print("Please enter a valid number.\n")

    elif user == "4":
        quit()
