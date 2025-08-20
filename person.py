class Person:
    number_of_people = 0
    """Represents a single person with their attributes."""
    def __init__(self, name, age, gender):
        Person.number_of_people += 1
        self.id = Person.number_of_people
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        """Returns a string representation of the person."""
        return f"Id: {self.id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

