topics = []

def add_topic():
    topic = input("Enter topic: ")
    #check if nag e exist na sya
    if topic not in topics:
        topics.append(topic)
        print("Topic added successfully!")
    else:
        print("That topic is already added")

def display_topics():
    if not topics:
        print("No topics yet")
        return False
    for i, topic in enumerate(topics, start=1):
        print(f"{i}. {topic}")
    return True


def view_topic():
   display_topics()


def edit_topic():
    if not display_topics():
        print("No topics to edit")
        return
    else:
            edited_topic = int(input("Enter topic id to edit: "))
            # check kung valid ba
            if 1 <= edited_topic <= len(topics):
                new_topic = input("Enter new topic: ")
                # replace old topics sa new
                topics[edited_topic - 1] = new_topic
                print("Topic updated successfully!")
            else:
                print("Invalid topic id")


def delete_topic():
    try:
        if not display_topics():
            print("No topics to delete")
            return
        else:
            delete = int(input("Enter topic id you want to delete: "))
            if 1 <= delete <= len(topics):
                # to delete correct topic
                index = topics.pop(delete - 1)
                print(f"'{index}' has been deleted.")
            else:
                print("Invalid topic id")
    except ValueError:
        print("Enter valid topic id")


def main_loop():
    while True:

        print("Select operation: \n1. Add Topic \n2. View Topic \n3. Edit Topic \n4. Delete Topic \n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_topic()

        elif choice == "2":
            view_topic()

        elif choice == "3":
            edit_topic()

        elif choice == "4":
            delete_topic()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_loop()