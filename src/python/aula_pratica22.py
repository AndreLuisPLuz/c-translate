from commons import get_valid_input

def calculate_monthly_salary(
        daily_hours: int,
        hour_value: float,
        days_worked: int) -> float :
    return daily_hours * hour_value * days_worked

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