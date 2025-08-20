import time
from save_people import save_people
from delete_people import delete_person_by_name
from load_people import load_people
from find_person import find_person
from add_person import add_person
from person_helpers import get_total_age, get_total_people, genders_sum, find_and_compare_people
from delete_all_people import delete_all_people    
from manage_people import change_person_details
# --- Main program flow ---
def main():
  

    people = load_people()
    while True:
        choice = input("\nDo you want to\n"
        " (A)dd\n"
        " (D)isplay all\n"
        " (F)ind a person\n"
        " (C)ompare people\n"
        " (M)anage people\n"
        " (O)ther options\n"
        " (Q)uit? \n"
        "> ").lower()
        
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

        elif choice == 'm':
            change_person_details(people)
        elif choice == 'o':
            while True:
                choice = input(
                            "\nWhat do you want to do?\n"
                            "  (T) Total people\n"
                            "  (S) Total age\n"
                            "  (D) Delete a person\n"
                            "  (DEL) Delete all people\n"
                            "  (R) Refresh list\n"
                            "  (M) Back to main menu\n"
                            "> "
                        ).lower()
                print("\n ---------")
                if choice == 't':
                    total_people = get_total_people() 
                    if total_people is not None:
                        print(f"There is a total of {total_people} people in the list.")
                        genders = genders_sum()
                    continue
                elif choice == 'r':
                    print("\n--- All People ---")
                    if not people:
                        print("No people to display.")
                    else:
                        for person in people:
                            print(person)
                        print("------------------")
            
                elif choice == 'd':
                    delete_person_by_name()
                    people = load_people()
                    continue
                elif choice == 's':
                    total_sum = get_total_age()
                    avg_age_int = get_total_age()
                    if total_sum is not None:
                        print(f"The total age of all people is: {total_sum[0]}.")
                        print(f"The average age is: {avg_age_int[1]}.")
                    continue
                elif choice == 'del':
                    confirmation = input("Are you sure you want to delete all people? (yes/no): ").lower()
                    if confirmation == 'yes':
                        delete_all_people()
                        people = []
                    else:
                        print("Deletion cancelled.")
                elif choice == 'm':
                    break


        elif choice == 'c':
            print("\n--- Compare People ---")
            find_and_compare_people()
        elif choice == 'f':
            print("\n--- Who are we looking for? ---")
            find_person(people)
        elif choice == 'q':
            save_people(people)
            print("Goodbye!")
            break

if __name__ == "__main__":
    print("Hello! Welcome to the People Manager.")
    print("Loading data...")
    start_time = time.time()
    
    people = load_people()
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"Data loaded. The operation took {duration:.4f} seconds.")
    main()