#   Add Contact using list dictionaries
#   Print All contacts

contacts = [
    {"name" : "kath", "phone" : "09923654701"},
]
name = input("Enter your name: ").title()
phone = input("Enter your phone number: ")

contacts.append({"name" : name, "phone" : phone})

for i, value in enumerate(contacts, start=1):
    print(f"{i}. {value['name']} : {value['phone']}")