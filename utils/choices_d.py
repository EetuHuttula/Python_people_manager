from utils.data_utils import get_every_apartment

def choice_d_options(people):
    """Choices from option D: Display people or apartments."""
    print("\n--- All People ---")
    if not people:
        print("No people to display.")
        return  # Exit early if no data

    choice = input(
        "\nDo you want to see\n"
        "(P)eople \n"
        "(A)partments \n"
    ).lower().strip()

    if choice == "p":
        # Sorting loop
        while True:
            sort_choice = input("Sort list by (N)ame, (A)ge, (G)ender or 'no' to skip: ").lower()
            if sort_choice == "n":
                people.sort(key=lambda person: person.name)
                print("List sorted by Name.")
                break
            elif sort_choice == "a":
                people.sort(key=lambda person: person.age)
                print("List sorted by Age.")
                break
            elif sort_choice == "g":
                people.sort(key=lambda person: person.gender)
                print("List sorted by Gender.")
                break
            elif sort_choice == "no":
                print("List not sorted.")
                break
            else:
                print("Invalid choice. Please enter 'n', 'a', 'g', or 'no'.")

        # Print list after sorting decision
        for person in people:
            print(person)

    elif choice == "a":
        # Show apartments (pass people list to function if needed)
        get_every_apartment(people)
        print("------------------")
    else:
        print("Invalid choice. Please enter P or A.")
