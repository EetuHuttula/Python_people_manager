import json 

def get_total_age(filename="people.json"):
    """sums ages, gets average age."""
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