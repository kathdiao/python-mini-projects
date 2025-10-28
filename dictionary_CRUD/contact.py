contacts = {}

while True:
    #trying this way para mag display ng options or choices
    print("\nSelect Operation:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            name = input("Enter contact name: ")
            if name in contacts:
                print("Contact already exists")
            else:
                phone = int(input("Enter phone number: "))
                contacts[name] = phone
                print(f"Contact '{name}' added successfully")
        except ValueError:
            print("Invalid input")
    elif choice == "2":
        if not contacts:
            print("No contacts yet!")
        else:
            print("All contacts:")
            for i, (name, phone) in enumerate(contacts.items(), start=1):
                print(f"{i}. {name} - {phone}")
    elif choice == "3":
        break
    else:
        print("Invalid input")
