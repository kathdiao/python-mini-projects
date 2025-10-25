task = []
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task \n4. Exit")
    #("\n1.) for choices lang
    choice = input("Enter your choice: ")
    if choice == "1":
        todo = input("Enter Task Name: ")
        task.append(todo)
        print("\nTask added")
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
        print("\nTask removed")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
