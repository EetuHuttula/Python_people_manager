from utils.imports import *

def choice_o_options(people):
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

