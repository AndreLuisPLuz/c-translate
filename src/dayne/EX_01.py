def Sal_Bruto(p_horasn, p_horase):
    respn = p_horasn * 12
    respe = p_horase * 15.5
    bruto = respn + respe

    return bruto

def Sal_Liquido(p_respbruto):
    respliquido = p_respbruto * 0.1
    respliquido = p_respbruto - respliquido
    return respliquido

def mostra(p_code,p_horasn,p_horase,p_respbruto,p_respliquido):
    print(f"O funcionário {p_code} trabalhou {p_horasn} horas normais e {p_horase} horas extras.\n")
    print(f"Irá receber R$ {p_respbruto:.2f} de salário bruto e R$ {p_respliquido:.2f} de salário líquido\n\n")


for i in range (1,11,1):
    cod = int(input("\nQUAL SEU CODIGO:"))
    horasn = float(input("\nQUANTIDADE DE HORAS NORMAIS:"))
    horase = float(input("\nQUANTIDADE DE HORAS EXTRAS:"))

    print("_________________________________________\n");
    print(f"\n{i}º FUNCIONARIO CALCULADO:\n")
    respbruto = Sal_Bruto(horasn, horase)
    respliquido = Sal_Liquido(respbruto)
    mostra(cod,horasn,horase,respbruto,respliquido)