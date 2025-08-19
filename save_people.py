import json
def save_people(people_list, filename="people.json"):
    """Saves a list of Person objects to a JSON file."""
    data_to_save = []
    for person in people_list:
        data_to_save.append({
            "name": person.name,
            "age": person.age,
            "gender": person.gender,
        })
    
    with open(filename, "w") as f:
        json.dump(data_to_save, f, indent=4)
    print("Data saved successfully.")
