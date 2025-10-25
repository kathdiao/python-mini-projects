movies = []
def add_movie():
    new_movie = input("Enter movie name: ")
    if new_movie not in movies:
        movies.append(new_movie)
        print("Movie added successfully")
    else:
        print("Movie already exists")


def display_movies():
    if not movies:
        print("No movies yet")
        return False
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")
        #automatic way para mag display, best practices para hindi na mag manual counter += 1
    return True


def view_movies():
    display_movies()


def edit_movie():
    display_movies()


    try:
        edit = int(input("Enter movie id to edit: "))
        if 1 <= edit <= len(movies):
            new_movie = input("Enter new movie name: ")
            movies[edit -1] = new_movie
            print("Movies updated successfully")
        else:
            print("Invalid movie number")
    except ValueError:
        print("Invalid movie number")


def delete_movie():
    if not display_movies():
        return
    try:
        delete = int(input("Enter movie number to delete: "))
        if 1 <= delete <= len(movies):
            removed = movies.pop(delete - 1)
            print(f"'{removed}' has been deleted.")
        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid movie number")


def main_loop():
    while True:
        print("Select Operations: \n1. Add movies \n2. View movies \n3. Edit movies \n4. Delete movies \n5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            view_movies()
        elif choice == "3":
            edit_movie()
        elif choice == "4":
            delete_movie()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_loop()