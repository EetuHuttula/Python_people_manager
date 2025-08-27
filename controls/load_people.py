import json
from person import Person

def load_people(filename="people.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            people = []
            for d in data:
                person = Person(
                    d["name"],
                    d["age"],
                    d["gender"],
                    d["sections"],
                    d["floor"],
                    d["apartment_number"],
                    d.get("building_address", "Rauninkatu 32")
                )
                people.append(person)
            return people
    except FileNotFoundError:
        print("No data file found. Starting empty.")
        return []
