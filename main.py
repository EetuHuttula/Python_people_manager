import json
from save_people import save_people
from load_people import load_people
from find_person import find_person
from add_person import add_person
from person_helpers import get_total_age, get_total_people, genders_sum
    
# --- Main program flow ---

people = load_people()

while True:
    choice = input("\nDo you want to (A)dd, (D)isplay all, (F)ind a person, or (Q)uit? ").lower()
    
    if choice == 'a':
        new_person = add_person()
        if new_person:
            people.append(new_person)
            save_people(people)
    elif choice == 'd':
        print("\n--- All People ---")
        if not people:
            print("No people to display.")
        else:
            for person in people:
                print(person)
        print("------------------")
        total_sum = get_total_age()
        if total_sum is not None:
            print(f"The total age of all people is: {total_sum}.")
        print("------------------")
        total_people = get_total_people()
        if total_people is not None:
            print(f"There is total of {total_people} people in the list.")
        print("------------------")
        genders = genders_sum()
        print("------------------")
    elif choice == 'f':
        find_person(people)
    elif choice == 'q':
        save_people(people)
        break
    else:
        print("Invalid choice. Please choose A, D, F, or Q.")