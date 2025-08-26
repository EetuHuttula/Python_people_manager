from save_people import save_people

def change_person_details(people):
    """Function to change a person's details."""
    name = input("Enter the name of the person you want to change: ")
    person_found = False

    for person in people:
        if person.name.lower() == name.lower():
            person_found = True
            print(f"Current details: {person}")

            changes_made = False

            # Get new name, check if not empty
            new_name_input = input("Enter new name (or press Enter to keep current): ").capitalize()
            if new_name_input:
                person.name = new_name_input
                changes_made = True

            # Get new age, check if not empty, and handle ValueError
            new_age_input = input("Enter new age (or press Enter to keep current): ")
            if new_age_input:
                try:
                    person.age = int(new_age_input)
                    changes_made = True
                except ValueError:
                    print("Invalid age entered. Keeping current age.")

            # Get new gender, check if not empty
            new_gender_input = input("Enter new gender (or press Enter to keep current): ").capitalize()
            if new_gender_input:
                person.gender = new_gender_input
                changes_made = True

            if changes_made:
                print(f"Updated details: {person}")
                save_people(people)
            else:
                print("No changes made.")
            return 
    if not person_found:
        print(f"Person with the name '{name}' was not found.")