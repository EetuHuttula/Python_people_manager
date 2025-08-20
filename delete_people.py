import json
def delete_person_by_name(filename="people.json"):
    """Deletes a person from the list by name."""
    search_name = input("Enter the name of the person you want to delete: ")
    found = False
    try:
        # Load the existing data
        with open(filename, "r") as f:
            data = json.load(f)

        # Create a new list without the person to be deleted
        new_data = [person for person in data if person["name"].lower() != search_name.lower()]
        
        # Check if a person was actually removed
        if len(new_data) < len(data):
            print(f"Deleting {search_name}...")
            # Overwrite the file with the new data
            with open(filename, "w") as f:
                json.dump(new_data, f, indent=4)
            print(f"Successfully deleted {search_name}.")
        else:
            print(f"Person with the name '{search_name}' was not found.")

    except FileNotFoundError:
        print("File not found. No people to delete.")
    except json.JSONDecodeError:
        print("Error reading the file. The file may be empty or corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")