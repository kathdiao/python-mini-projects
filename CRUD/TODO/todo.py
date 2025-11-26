task = []
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        todo = input("Enter Task Name: ")
        task.append(todo)
        print("Task added")
    elif choice == "2":
        print("All tasks: ")
        counter = 1
        for t in task:
            print(f" {counter}. {t}")
            counter += 1
            #for loop naman para sa pag print ng maayos and readable tasks
    elif choice == "3":
        question = int(input("Which task would you like to remove?: "))
        index = question - 1
        task.pop(index)
        print("Task removed")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
