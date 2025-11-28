#    Simple contact editor focused on editing phone numbers and names
contacts = [
    {"name": "Katherine", "phone": "09923654701"},
    {"name": "Tala", "phone": "09923654702"},
    {"name": "Jea", "phone": "09923654703"}
]

for items, value in enumerate(contacts, start=1):
    print(f"{items}. {value['name']} : {value['phone']}")

print("EDIT Contact")
print("1. Edit Phone number")
print("2. Edit Name")
print("3. Exit")

user_input = input("Enter your choice 1/2?: ")

if user_input == "1":
    edit = input("Enter contact name you want to change: ").title()

    for i in range(len(contacts)):
        if contacts[i]['name'] == edit:
            new_phone = input("Enter new phone number: ")
            contacts[i]['phone'] = new_phone
            print("Contact changed successfully")

            for item, val in enumerate(contacts, start=1):
                print(f"{item}. {val['name']} : {val['phone']}")

elif user_input == "2":

    edit_name = input("What name would you like to change? ").title()

    for i in range(len(contacts)):
        if edit_name == contacts[i]["name"]:
            new_name = input("Enter new name: ").title()
            contacts[i]["name"] = new_name
            print("Name updated successfully!")

            for t, v in enumerate(contacts, start=1):
                print(f"{t}: {v['name']} : {v['phone']}")

elif user_input == "3":
    quit()