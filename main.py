import json
from save_people import save_people
from get_total_people import get_total_people
from load_people import load_people
from person import Person

    
def get_total_age(filename="people.json"):
    total_age = 0
    try:
        with open(filename, "r") as f:
            people_list = json.load(f)
            
            for person in people_list:
                total_age += person.get('age', 0)
        return total_age
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filename}'.")
        return None
def get_total_people(filename="people.json"):
    try:
        with open(filename, "r") as f:
            people_list = json.load(f)
        return len(people_list)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filename}'.")
        return None
    
def genders_sum(filename="people.json"):
    male_count = 0
    female_count = 0
    try:
        with open(filename, "r") as f:
            people_list= json.load(f)
            for person in people_list:
                gender = person.get('gender', '').lower()
                if gender == 'male':
                    male_count += 1
                elif gender == 'female':
                    female_count += 1
        print(f"There are {male_count} males and {female_count} females.")
        if male_count > female_count:
            print("There are more males in the list.")
        elif female_count > male_count:
            print("There are more females in the list.")
        else:
            print("The number of males and females is equal.")
        return male_count, female_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filename}'.")
        return None    
    
def add_person():
    """Prompts the user for a new person's details and returns a Person object."""
    try:
        name = input("Lisää nimi: ")
        age = int(input("Lisää ikä: "))
        gender = input("Lisää sukupuoli: ")
        return Person(name, age, gender)
    except ValueError:
        print("Invalid input. Please enter numbers for age, length, and weight.")
        return None

def find_person(people_list):
    """Finds and prints a person's details by name."""
    search_name = input("Enter the name of the person you want to find: ")
    found = False
    for person in people_list:
        # We'll do a case-insensitive search to make it more user-friendly
        if person.name.lower() == search_name.lower():
            print("\nPerson found:")
            print(person)
            found = True
            break # Exit the loop once a match is found
    
    if not found:
        print(f"\nNo person found with the name '{search_name}'.")

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