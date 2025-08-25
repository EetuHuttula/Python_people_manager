def choice_d_options(people):
    print("\n--- All People ---")
    if not people:
        print("No people to display.")
    else:
        while True:
            sort_choice = input("Sort list by (N)ame, (A)ge or (G)ender? Enter 'no' to skip: ").lower()
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
        
        for person in people:
            print(person)
        print("------------------")