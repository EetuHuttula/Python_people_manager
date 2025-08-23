def find_and_compare_people(people_list):
    """Finds and prints a person's details by name."""
    search_name = input("Enter the name of the person you want to compare: ")
    search_name2 = input("Enter the name of the second person you want to compare: ")
    found = False
    for person in people_list:
        if person.name.lower() == search_name.lower():
            print("\nPersons found:")
            print(person)
            found = True 
            for person2 in people_list:
                if person2.name.lower() == search_name2.lower():
                    print(person2) 
                    found = True

                    #Age comparison
                    if person.age > person2.age:
                        older = person.age - person2.age
                        print(f"{person.name} is {older} year older than {person2.name}.")
                    elif person.age < person2.age:
                        older = person2.age - person.age
                        print(f"{person2.name} is {older} year older than {person.name}.")
                    else:
                        print(f"{person.name} and {person2.name} are of the same age.")
                    #Gender comparison
                    if person.gender == person2.gender:
                        print(f"Both {person.name} and {person2.name} are {person.gender}s.")
                    else:
                        print(f"{person.name} is a {person.gender} and {person2.name} is a {person2.gender}.")
                    break
            break
    if not found:
        print(f"\nNo person found with the name '{search_name}'.")