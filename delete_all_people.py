import json
from person import Person
def delete_all_people(people, filename="people.json"):
    """
    Clears the in-memory list and deletes all data from the JSON file.
    """
    try:
        # Clear the in-memory list
        people.clear()
        Person.number_of_people = 0
        # Overwrite the file with an empty list
        with open(filename, "w") as f:
            json.dump([], f, indent=4)

        print("All people have been deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")
