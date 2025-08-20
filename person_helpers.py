import json

def get_total_age(filename="people.json"):
    total_age = 0
    try:
        with open(filename, "r") as f:
            people_list = json.load(f)
            
            for person in people_list:
                total_age += person.get('age', 0)
                avg_age = total_age / len(people_list)
                avg_age_int = round(avg_age)
        return total_age, avg_age_int
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
    
def find_and_compare_people(people_list):
    """Finds and prints a person's details by name."""
    search_name = input("Enter the name of the person you want to compare: ")
    search_name2 = input("Enter the name of the second person you want to compare: ")
    found = False
    for person in people_list:
        if person.name.lower() == search_name.lower():
            print("\nPersons found:")
            print(person)
            found = True 
            for person2 in people_list:
                if person2.name.lower() == search_name2.lower():
                    print(person2) 
                    found = True
                    if person.age > person2.age:
                        print(f"{person.name} is older than {person2.name}.")
                    elif person.age < person2.age:
                        print(f"{person2.name} is older than {person.name}.")
                    else:
                        print(f"{person.name} and {person2.name} are of the same age.")

                    if person.gender == person2.gender:
                        print(f"Both {person.name} and {person2.name} are {person.gender}s.")
                    else:
                        print(f"{person.name} is a {person.gender} and {person2.name} is a {person2.gender}.")
                    break
            break
    if not found:
        print(f"\nNo person found with the name '{search_name}'.")

