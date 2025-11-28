#   Edit Contact using list dictionaries
#   Print All contacts
contacts = [
    {"name": "Katherine", "phone": "09923654701"},
    {"name": "Tala", "phone": "09923654702"},
    {"name": "Jea", "phone": "09923654703"}
]

user = input("What do contact you want to delete?: ")

for contact in contacts:
    if contact["name"] == user.title():
        contacts.remove(contact)
        print(f"Contact {user} has been deleted")
        break
else:
    print(f"Contact {user} does not exist")

for item, value in enumerate(contacts, start=1):
    print(f"{item}: {value['name']} : {value['phone']}")

