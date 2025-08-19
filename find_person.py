def find_person(people_list):
    """Finds and prints a person's details by name."""
    search_name = input("Enter the name of the person you want to find: ")
    found = False
    for person in people_list:
        # We'll do a case-insensitive search to make it more user-friendly
        if person.name.lower() == search_name.lower():
            print("\nPerson found:")
            print(person)
            found = True
            break # Exit the loop once a match is found
    
    if not found:
        print(f"\nNo person found with the name '{search_name}'.")