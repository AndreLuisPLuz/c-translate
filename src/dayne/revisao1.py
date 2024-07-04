
idadesoma = 0;
cont = 0;
media = 0;
numtimes = 0;

codtime = int(input("Qual o Código do seu Time:\n"))

while(codtime > 0):
    for cont in range(0,3,1):
        nome = input("Qual seu nome: \n")
        idade = int(input("Qual sua idade: \n"))
        print(f"Obrigado pelo cadastro {nome}\n\n")
        idadesoma += idade
    numtimes += 1
    media = idadesoma / 3
    print(f"A media de idade deste time é de {media: .2f} anos.\n")
    print(f"{numtimes}º time calculado.\n\n")
	
    idadesoma = 0
	
    codtime = int(input("Qual o Código do seu Time:\n"))

print(f"\nO número de times cadastrados é de : {numtimes} times.\n\n");


