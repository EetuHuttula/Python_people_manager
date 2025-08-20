Python People Manager 📝

This is a simple console-based application for managing a list of people. You can add new people, view existing ones, and update or delete their details. All data is stored in a people.json file.
Features ✨

    Add New People: Enter details for a new person (name, age, gender).

    Display People: View a formatted list of all people stored in the application.

    Update Details: Change the name, age, or gender of an existing person.

    Delete a Person: Remove a specific person from the list.

    Clear All Data: Delete all people from the people.json file.

    View Statistics: See the total number of people and their average age.

How It Works ⚙️

The application loads all people data from a people.json file when it starts. All changes—adding, updating, or deleting—are applied to the in-memory list first and then saved back to the people.json file to ensure the data is always up to date.
Getting Started 🚀
Prerequisites

    Python 3.6 or newer

Usage

    Run the application: Navigate to the directory containing main.py in your terminal and run the following command:

    python main.py

    Follow the menu: The application will present a menu with several options. Simply enter the corresponding letter to perform an action. For example, enter a to add a new person.

File Structure 📁

    main.py: The main program loop and user interface.

    person.py: Defines the Person class.

    add_person.py: Contains the function to add a new person.

    load_people.py: Handles loading data from people.json.

    save_people.py: Handles saving data to people.json.

    delete_person.py: Contains the function to delete a single person.

    delete_all_people.py: Contains the function to delete all people.

    find_person.py: Contains the function to find a specific person.

    person_helpers.py: Contains helper functions for various statistics and comparisons.

    people.json: The data file where all person information is stored.

    .gitignore: Specifies which files should be ignored by Git (e.g., people.json).

Contributing 🤝

Contributions are welcome! If you find a bug or have an idea for a new feature, please submit an issue or a pull request.
