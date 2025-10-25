movies = []
while True:
    print("Select Operations: \n1. Add movies \n2. View movies \n3. Edit movies \n4. Delete movies \n5. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        movies.append(input("Enter movie name: "))
        print("Movies added")
    elif choice == "2":
        if not movies:
            print("No movies yet")
        else:
            print("All movies: ")
            counter = 1
            for m in movies:
                print(f" {counter}. {m}")
                counter += 1
                # manual way para mag display
    elif choice == "3":
        if not movies:
            print("No movies yet")
        else:
            print("All movies: ")
            counter = 1
            for movie in movies:
                print(f" {counter}. {movie}")
                counter += 1

            edit = int(input("Enter movie id to edit: "))
            if 1 <= edit <= len(movies):
                new_movie = input("Enter new movie name: ")
                movies[edit -1] = new_movie
                print("Movies updated successfully")
            else:
                print("Invalid movie number")
    elif choice == "4":
        if not movies:
            print("No movies yet")
        else:
            print("All movies: ")
            for i, m in enumerate(movies, start=1):
                print(f"{i}. {m}")
            delete = int(input("Enter movie number to delete: "))
            if 1 <= delete <= len(movies):
                removed = movies.pop(delete - 1)
                print(f"'{removed}' has been deleted.")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
