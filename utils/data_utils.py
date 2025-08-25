def is_occupied(people_list, section, floor, apartment_number):
    """Check if the apartment is already occupied."""
    for resident in people_list:
        if (resident.sections == section and
            resident.floor == floor and
            resident.apartment_number == apartment_number):
            return True
    return False