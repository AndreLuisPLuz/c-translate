def N(p_num):
    acumulo = 0
    if(p_num > 0 ):
        print(f"\n{p_num} é um dos número.\n")
        acumulo = N(p_num - 1) + p_num
    return acumulo

num = int(input("\nINFORME UM NUMERO INTEIRO POSITIVO: "));
resp = N(num)

print(f"\n{resp} é o somatório dos numeros.")