"""
People manager CLI Application.
"""
import time
from utils.find_person import find_person
from controls.add_person import add_person
from controls.manage_people import change_person_details
from save_people import save_people
from controls.load_people import load_people
from utils.compare_people import find_and_compare_people
from utils.choices_d import choice_d_options
from utils.choices_o import choice_o_options

def main(people):
    """
    Main program flow
    """
    def add_action():
        new_person = add_person(people)
        if new_person:
            people.append(new_person)
            save_people(people)
    menu_actions = {
        'a': add_action,
        'd': lambda: choice_d_options(people),
        'm': lambda: change_person_details(people),
        'o': lambda: choice_o_options(people),
        'c': lambda: find_and_compare_people(people),
        'f': lambda: find_person(people),
        }

    while True:

        choice = input(
            "\nDo you want to\n"
            " (A)dd\n"
            " (D)isplay all\n"
            " (F)ind a person\n"
            " (C)ompare people\n"
            " (M)anage people\n"
            " (O)ther options\n"
            " (Q)uit?\n> "
        ).lower().strip()

        if choice == 'q':
            print("Goodbye!")
            break
        action = menu_actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Hello! Welcome to the People Manager.")
    print("Loading data...")
    start_time = time.time()
    people = load_people()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Data loaded. The operation took {duration:.4f} seconds.")
    try:
        main(people)
    except KeyboardInterrupt:
        print("\nInterrupted! Saving data and exiting...")
        save_people(people)
        print("Data saved. Goodbye!")
