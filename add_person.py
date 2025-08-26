from person import Person
from utils.data_utils import is_occupied, is_every_apartment_full
from load_people import load_people

def add_person(people_list):
    """Prompts the user for a new person's details and returns a Person object."""
    try:
        residents = load_people()
        if is_every_apartment_full(residents):
            print("All apartments are occupied.")
            return None
        elif residents is not None:
            for i in range(len(residents)):
                apartments = 18
                i += 1 
                left = apartments - i
                continue
        print(f"There is still {left} apartments left.")

        name = input("Name: ").strip().capitalize()
        age = int(input("Age: "))
        gender = input("Gender: ").strip().capitalize()
        section = input("Section (A or B): ").upper()

        if section not in ("A", "B"):
            print("Invalid section. Must be A or B.")
            return None
        
        floor = int(input("Floor (1-3): "))
        if floor not in (1, 2, 3):
            print("Invalid floor. Must be 1, 2, or 3.")
            return None
        

        # Determine valid apartment numbers based on floor
        valid_apartments = {1: (1, 2, 3), 2: (4, 5, 6), 3: (7, 8, 9)}
        apartment_number = int(input(f"Apartment number ({valid_apartments[floor][0]}-{valid_apartments[floor][-1]}): "))
        if apartment_number not in valid_apartments[floor]:
            print(f"Invalid apartment number for floor {floor}.")
            return None
        
        if is_occupied(people_list, section, floor, apartment_number, street_address = "rauninkatu 32"):
            print("This apartment is already occupied!")
            return None
        return Person(name, age, gender, section, floor, apartment_number)
    
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None
