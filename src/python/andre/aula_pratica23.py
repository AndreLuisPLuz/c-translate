import sys
import os
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(os.path.realpath(current_dir))
sys.path.append(root_dir)

from commons import get_valid_input  # noqa: E402

def liters_to_fuel(
        liter_value: float, value_chosen: float
) -> float:
    return value_chosen / liter_value

if __name__ == "__main__":
    chosen_value = get_valid_input(
        "Qual o valor que gostaria de abaster?\n",
        float
    )

    liter_value = get_valid_input(
        "Qual o valor do litro da gasolina?\n",
        float
    )

    liters_filled = liters_to_fuel(
        liter_value, chosen_value
    )

    print(f"Você irá abastercer {liters_filled:.3f} litros.")