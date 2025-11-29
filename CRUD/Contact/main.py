#   Main
#   List Dictionaries
contacts = [
    {"name": "Kath", "phone": "09923654701"},
]

while True:
    print("\nSelect Operation:") 
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ").title()
        phone = input("Enter your phone number: ")

        contacts.append({"name": name, "phone": phone})

        for item, value in enumerate(contacts, start=1):
            print(f"{item}. {value['name']} : {value['phone']}")

    elif choice == "2":
        if not contacts:
            print("No contacts added yet")
        else:
            for item, value in enumerate(contacts, start=1):
                print(f"{item}. {value['name']} : {value['phone']}")

    elif choice == "3":
        print("Select Operation:"
              "\n1. Edit Name"
              "\n2. Edit Phone")
        user = input("What do you want to edit?: ")

        if user == "1":
            edit_name = input("What name would you like to change? ").title()

            for i in range(len(contacts)):
                if edit_name == contacts[i]["name"]:
                    new_name = input("Enter new name: ").title()
                    contacts[i]["name"] = new_name
                    print("Name updated successfully!")

                    for t, v in enumerate(contacts, start=1):
                        print(f"{t}: {v['name']} : {v['phone']}")
        elif user == "2":
            edit = input("Enter contact name you want to change: ").title()

            for i in range(len(contacts)):
                if contacts[i]['name'] == edit:
                    new_phone = input("Enter new phone number: ")
                    contacts[i]['phone'] = new_phone
                    print("Contact changed successfully")

                    for item, val in enumerate(contacts, start=1):
                        print(f"{item}. {val['name']} : {val['phone']}")

    elif choice == "4":
        user = input("What contact do you want to delete?: ")

        for contact in contacts:
            confirm = input("Do you really want to delete this contact? y/n: ")
            if confirm == "y":
                if contact["name"] == user.title():
                    contacts.remove(contact)
                    print(f"Contact {user} has been deleted")
                    break
            else:
                print("Deletion cancelled")
        else:
            print(f"Contact {user} does not exist")

        for item, value in enumerate(contacts, start=1):
            print(f"{item}: {value['name']} : {value['phone']}")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please select from 1–5.")
