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