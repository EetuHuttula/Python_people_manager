
from person import Person


def add_person():
    """Prompts the user for a new person's details and returns a Person object."""
    try:
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        return Person(name, age, gender)
    except ValueError:
        print("Invalid input. Please enter numbers for age, length, and weight.")
        return None
