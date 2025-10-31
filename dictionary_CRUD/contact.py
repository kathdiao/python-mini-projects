contacts = {}

while True:
    #other way to print operations
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
                print("Contact already exists!")
            else:
                phone = int(input("Enter phone number: "))
                contacts[name] = phone
                print(f"Contact '{name}' added successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "2":
        if not contacts:
            print("No contacts yet!")
        else:
            print("\nAll contacts:")
            #ina access ng contacts.items yung key value pair
            for i, (name, phone) in enumerate(contacts.items(), start=1):
                print(f"{i}. {name} - {phone}")

    elif choice == "3":
        if not contacts:
            print("No contacts to edit!")
        else:
            name = input("Enter contact name to edit: ")
            if name in contacts:
                try:
                    new_phone = int(input("Enter new phone number: "))
                    contacts[name] = new_phone
                    print(f"Contact '{name}' updated successfully!")
                except ValueError:
                    print("Invalid number. Please try again.")
            else:
                print("Contact not found!")

    elif choice == "4":
        if not contacts:
            print("No contacts to delete!")
        else:
            name = input("Enter contact name to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact '{name}' deleted successfully!")
            else:
                print("Contact not found!")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please select from 1–5.")
