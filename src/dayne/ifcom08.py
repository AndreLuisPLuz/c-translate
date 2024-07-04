idade = int(input("QUAL A IDADE: \n"))
sexo = input("QUAL O SEXO, (M) PARA MASCULINO OU (F) PARA FEMININO: \n")

match sexo:
    case "M":
        if(idade >= 16):
            print("voce tem direito a compra de ingressos \n")
        else:
            print("voce nao pode comprar ingressos \n")
    case "F":
        if(idade >= 18):
            print("voce tem direito a compra de ingressos \n")
        else:
            print("voce nao pode comprar ingressos \n")
    case _:
         print("essa opcao eh invalida!")
         print("fechou")

