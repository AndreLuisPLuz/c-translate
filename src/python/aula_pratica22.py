def calculate_monthly_salary(
        daily_hours: int,
        hour_value: float,
        days_worked: int) -> float :
    return daily_hours * hour_value * days_worked
    
def get_valid_input(prompt: str, type: object) -> object:
    """Asks user for input until a valid value is given."""

    is_valid_input = False
    while not is_valid_input:
        try:
            user_input = type(input(prompt))
            is_valid_input = True
        except ValueError:
            print("Entrada inválida. Tente novamente!")
    
    return user_input

if __name__ == '__main__':
    daily_hours = get_valid_input(
        "Qual a quantidade de horas trabalhadas por dia?\n",
        int
    )
    
    hour_value = get_valid_input(
        "Qual o valor da hora trabalhada?\n",
        float
    )

    days_worked = get_valid_input(
        "Quantos dias foram trabalhados?\n",
        int
    )
    
    monthly_salary = calculate_monthly_salary(
        daily_hours, hour_value, days_worked
    )

    print(f"O salário a ser pago é de R${monthly_salary:.2f}")