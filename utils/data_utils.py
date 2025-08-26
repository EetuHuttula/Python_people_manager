def is_occupied(people_list, section, floor, apartment_number, street_address):
    """Check if the apartment is already occupied."""
    for resident in people_list:
        if (resident.sections == section and
            resident.floor == floor and
            resident.apartment_number == apartment_number):
            return True
    return False

def is_every_apartment_full(people_list):
    valid_apartments = {1: (1,2,3,), 2: (4,5,6), 3: (7,8,9)}

    for sections in ["A", "B"]:
        for floor in (1,2,3):
            for apt in valid_apartments[floor]:
                occupied = any(
                    p.sections == sections and
                    p.floor == floor and
                    p.apartment_number == apt
                    for p in people_list
                )
                if not occupied:
                    print("Apartments taken: ")
                    for p in people_list:
                        people_list.sort(key=lambda p : p.sections)
                        print(f"{p.street_address} Section: {p.sections}, Floor:  {p.floor}, Apartment number: {p.apartment_number}")
                    return False
    return True