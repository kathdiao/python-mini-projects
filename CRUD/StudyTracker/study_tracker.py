topics = []

while True:
    print("Select operation: \n1. Add Topic \n2. View Topic \n3. Edit Topic \n4. Delete Topic \n5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        topic = input("Enter topic: ")
        #check if nag e exist na sya
        if topic not in topics:
            topics.append(topic)
            print("Topic added successfully!")
        else:
            print("That topic is already added")

    elif choice == "2":
        if not topics:
            print("No topics yet")
        else:
            # automatic na may count
            for i, topic in enumerate(topics, start=1):
                print(f" {i}. {topic}")

    elif choice == "3":
        if not topics:
            print("No topics to edit")
        else:
            try:
                edited_topic = int(input("Enter topic id to edit: "))
                #ichecheck kung valid ba yung number
                if 1 <= edited_topic <= len(topics):
                    new_topic = input("Enter new topic: ")
                    #replace old topics sa new
                    topics[edited_topic -1] = new_topic
                    print("Topic updated successfully!")
                else:
                    print("Invalid topic id")
            except ValueError:
                print("Enter valid topic id")

    elif choice == "4":
        try:
            if not topics:
                print("No topics to delete")
            else:
                delete = int(input("Enter topic id you want to delete: "))
                if 1 <= delete <= len(topics):
                    #to delete yung correct topic
                    index = topics.pop(delete - 1)
                    print(f"'{index}' has been deleted.")
                else:
                    print("Invalid topic id")
        except ValueError:
            print("Enter valid topic id")

    elif choice == "5":
        break