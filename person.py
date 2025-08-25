class Person:
    number_of_people = 0
    """Represents a single person with their attributes."""
    def __init__(self, name, age, gender, sections, floor, apartment_number, street_address = "Rauninkatu 32"):

        Person.number_of_people += 1
        self.id = Person.number_of_people
        self.name = name
        self.age = age
        self.gender = gender
        
        #Apartment info
        self.sections = sections
        self.floor = floor
        self.apartment_number = apartment_number
        self.street_address = street_address

    def __str__(self):
        """Returns a string representation of the person."""
        return (
            f"Id: {self.id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
            f"Address: {self.street_address} {self.sections} {self.apartment_number}"
        )

