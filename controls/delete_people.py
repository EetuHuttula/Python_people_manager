import json
def delete_person_by_name(people, filename="people.json"):
    """Deletes a person from the in-memory list and updates the JSON file."""
    search_name = input("Enter the name to delete: ").strip()
    removed = False

    # Iterate over a copy to safely remove items from the list
    for p in people[:]:
        if p.name.lower() == search_name.lower():  # <-- use attribute, not .get()
            people.remove(p)
            removed = True

    if removed:
        # Save updated list to file
        with open(filename, "w") as f:
            json.dump([person.__dict__ for person in people], f, indent=4)
        print(f"Successfully deleted {search_name}.")
    else:
        print(f"Person '{search_name}' not found.")