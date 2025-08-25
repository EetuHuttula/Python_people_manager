import json
def genders_sum(filename="people.json"):
    """Sums genders."""
    male_count = 0
    female_count = 0
    try:
        with open(filename, "r") as f:
            people_list= json.load(f)
            for person in people_list:
                gender = person.get('gender', '').lower()
                if gender == 'male':
                    male_count += 1
                elif gender == 'female':
                    female_count += 1
        print(f"There are {male_count} males and {female_count} females.")
        if male_count > female_count:
            print("There are more males in the list.")
        elif female_count > male_count:
            print("There are more females in the list.")
        else:
            print("The number of males and females is equal.")
        return male_count, female_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filename}'.")
        return None  