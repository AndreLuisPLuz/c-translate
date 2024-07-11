import sys
import os
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(os.path.realpath(current_dir))
sys.path.append(root_dir)

from commons import get_valid_input  # noqa: E402
from statistics import mean # noqa: E402

def calculate_avg(values: list) -> float:
    return mean(values)

if __name__ == "__main__":
    hours_per_day = list()

    for i in range(5):
        hours = get_valid_input(
            f"Insira as horas trabalhadas no {i+1}° dia: ",
            int
        )

        hours_per_day.append(hours)
    
    average = calculate_avg(hours_per_day)
    print(f"A média de horas trabalhadas é de {average:.2f}")
    
