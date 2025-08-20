import time
def find_person(people_list):
    """Finds and prints a person's details by name."""
    
    print("\n--- Find Person ---")
    search_name = input("Enter the name of the person you want to find: ")
    found = False
    for person in people_list:
        # We'll do a case-insensitive search to make it more user-friendly

        start_time = time.time()

        if person.name.lower() == search_name.lower():
            print("\nPerson found:")

            print(person)

            found = True

            end_time = time.time()
            duration = end_time - start_time
            print(f"Search completed in {duration:.4f} seconds.")

            break # Exit the loop once a match is found
    
    if not found:
        print(f"\nNo person found with the name '{search_name}'.")