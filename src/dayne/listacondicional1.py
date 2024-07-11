
nome = input("Qual seu nome?\n")

idade = int(input("Qual sua idade?\n"))
sexo = input("Informe seu sexo(M-masculino / F-feminino): \n")

print(f"O nome fornecido foi: {nome} \n")
print(f"A idade fornecida foi: {idade} \n")
print(f"O sexo informado foi: {sexo} \n\n")

if(sexo =='M'):
	if(idade >= 18 and idade <= 65):
		print(f"{nome} , está compreendido(a) entre 18 e 65 anos de idade e é do sexo masculino.\n");
	

elif(sexo == 'F'):
	print(f"{nome} ,ou não está entre 18 e 65 anos de idade e/ou não é masculino. \n");
