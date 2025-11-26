#  Focused on editing phone number inside list dictionaries
contacts = [
    {"name": "Katherine", "phone": "09923654701"},
    {"name": "Tala", "phone": "09923654702"},
    {"name": "Jea", "phone": "09923654703"}
]

for item, value in enumerate(contacts, start=1):
    print(f"{item}. {value['name']} : {value['phone']}")

# yung name yung icacall and change ng phone number
edit = input("Enter contact name you want to change: ").title()

#   run loop to check isa isa yung nasa loob ng list_dict
for i in range(len(contacts)):
    if contacts[i]['name'] == edit:
        new_phone = input("Enter new phone number: ")
        contacts[i]['phone'] = new_phone
        print("Contact changed successfully")

        for item, value in enumerate(contacts, start=1):
            print(f"{item}. {value['name']} : {value['phone']}")

