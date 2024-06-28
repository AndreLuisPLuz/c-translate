alt = float(input("Qual a altura da pessoa? \n"));
num_pessoas = 0;
resp = 0;

while(alt > 0):
    sexo = input("Qual o sexo da pessoa?(M)Homens/(F)Mulheres \n");
    num_pessoas = num_pessoas + 1;

    match sexo:
        case "M":
            resp = (72.7*alt)-58;
            print(f"Seu peso ideal é de: {resp} kilos \n\n\n");
        case "F":
            resp = (62,1*alt)-44.7;
            print(f"Seu peso ideal é de: {resp} kilos \n\n\n");
        case _:
            print("opção inválida");
    alt = float(input("Qual a altura da pessoa? \n"));

print(f"{num_pessoas} participantes. /n/n");
