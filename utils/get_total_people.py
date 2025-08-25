import json
def get_total_people(filename="people.json"):
    """finds all people."""
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