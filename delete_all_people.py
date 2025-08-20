import json

def delete_all_people(filename="people.json"):
    """
    Deletes all data from the people.json file by overwriting it with an empty list.
    """
    try:
        with open(filename, "w") as f:
            # Overwrite the file with an empty list
            json.dump([], f, indent=4)
        print("All data has been deleted from the file.")
    except Exception as e:
        print(f"An error occurred: {e}")