import json
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()


def generate_work_items():
    items = []

    # Define possible work item types and states
    work_item_types = ["Bug", "Epic", "Feature",
                       "Impediment", "Release", "Task", "Test Case"]
    work_item_states = ["New", "To Do", "In Progress", "Committed"]
    assigned_to_names = ["Bill Wang", "Gavin", "Kaibo", "Evan", "Varad"]

    # Generate items assigned to your name
    # Generate items assigned to random names
    for _ in range(50):
        item = {
            "type": random.choice(work_item_types),
            "description": fake.paragraph(nb_sentences=2),
            "title": fake.catch_phrase(),
            "CreatedDate": (datetime.utcnow() - timedelta(days=random.randint(0, 7))).isoformat() + "Z",
            "url": f"https://dev.azure.com/yunchuwang5/4a8a1a08-7368-489f-857e-ac4a73a6ab68/_apis/wit/workItems/{random.randint(1, 100)}",
            "assigned_to": random.choice(assigned_to_names),
            "state": random.choice(work_item_states)
        }
        items.append(item)

    return items


def main():
    items = generate_work_items()

    # Save items to a JSON file
    with open("items.json", "w") as file:
        json.dump(items, file, indent=4)


if __name__ == "__main__":
    main()
