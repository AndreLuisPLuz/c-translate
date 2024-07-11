import sys
import os
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(os.path.realpath(current_dir))
sys.path.append(root_dir)

from commons import get_valid_input  # noqa: E402

def get_multiplication_table(num: int) -> list:
    nums = list(range(1, 11))
    return list(map(lambda n: num * n, nums))

if __name__ == "__main__":
    num = get_valid_input(
        "Insira o número cuja tabuada deseja obter: ",
        int
    )

    multiplication_table = get_multiplication_table(num)

    print("Tabuada:")
    for i in range(len(multiplication_table)):
        print(f"{num} x {i+1} = {multiplication_table[i]}")