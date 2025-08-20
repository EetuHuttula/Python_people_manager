import json
from person import Person

def load_people(filename="people.json"):
    """Loads people data from a JSON file and returns a list of Person objects."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            people_list = []
            for person_data in data:
                new_person = Person(
                    person_data["name"],
                    person_data["age"],
                    person_data["gender"]
                )
                people_list.append(new_person)
            return people_list
            
    except FileNotFoundError:
        print("No existing data file found. Starting with an empty list.")
        return []