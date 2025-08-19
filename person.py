class Person:
    """Represents a single person with their attributes."""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        """Returns a string representation of the person."""
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

