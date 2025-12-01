#   Main
#   List Dictionaries
contacts = [
    {"name": "Kath", "phone": "09923654701"},
]

def add_contact():
    name = input("Enter your name: ").title()
    phone = input("Enter your phone number: ")

    contacts.append({"name": name, "phone": phone})
    for item, value in enumerate(contacts, start=1):
        print(f"{item}. {value['name']} : {value['phone']}")


def view_contacts():
    if not contacts:
        print("No contacts added yet")
    else:
        for item, value in enumerate(contacts, start=1):
            print(f"{item}. {value['name']} : {value['phone']}")


def edit_contact():
    edit_name = input("What name would you like to change? ").title()

    for i in range(len(contacts)):
        if edit_name == contacts[i]["name"]:
            new_name = input("Enter new name: ").title()
            contacts[i]["name"] = new_name
            print("Name updated successfully!")
            return

    print(f"Contact {edit_name} does not exist")


def delete_contact():
    user = input("What contact do you want to delete?: ")

    for contact in contacts:
        if contact["name"] == user.title():
            confirm = input("Do you really want to delete this contact? y/n: ")
            if confirm == "y":
                contacts.remove(contact)
                print(f"Contact {user} has been deleted")
            else:
                print("Deletion cancelled")
            return

    print(f"Contact {user} does not exist")
    view_contacts()


def main():
    while True:
        print("\nSelect Operation:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            edit_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()