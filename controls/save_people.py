import json
import time
def save_people(people_list, filename="people.json"):
    data = []
    for p in people_list:
        start_time = time.time()
        data.append({
            "name": p.name,
            "age": p.age,
            "gender": p.gender,
            "street_address": p.street_address,
            "sections": p.sections,
            "floor": p.floor,
            "apartment_number": p.apartment_number
        })

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print("Data saved successfully.")
    end_time = time.time()
    duration = end_time - start_time
    print(f"Person saved to json in {duration:.4f} seconds.")
