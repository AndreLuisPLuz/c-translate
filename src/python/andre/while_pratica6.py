import sys
import os
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(os.path.realpath(current_dir))
sys.path.append(root_dir)

from commons import get_valid_input  # noqa: E402

def initialize_categories() -> dict:
    categories = {
        "Infantil A": 0,
        "Infantil B": 0,
        "Juvenil A": 0,
        "Juvenil B": 0,
        "Adulto": 0
    }

    return categories

def classify(age: int, categories: dict) -> None:
    category = str()

    if age >= 5 and age <= 7:
        category = "Infantil A"
    elif age <= 10:
        category = "Infantil B"
    elif age <= 13:
        category = "Juvenil A"
    elif age <= 17:
        category = "Juvenil B"
    else:
        category = "Adulto"
    
    categories[category] += 1

if __name__ == "__main__":
    categories = initialize_categories()

    age = -1
    i = 0
    while age != 0:
        age = get_valid_input(
            f"Qual a idade do {i+1}° nadador? ",
            int
        )
    
        classify(age, categories)
        i += 1
    
    print("\nClasses\n")

    for key in categories.keys():
        print(f"{key}: {categories[key]}")