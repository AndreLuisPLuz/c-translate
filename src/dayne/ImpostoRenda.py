salL = 0
salIR = 0
valorINSS = 0
valorIR = 0
somaINSS = 0
somaIR = 0

cod = int(input("Digite o código do funcionário: "))

while(cod != 0):
    dep = int(input("Digite o numero de Dependentes: "))

    for i in range(1,13,1):
        salB = float(input(f"Digite o {i}° Salario Bruto= "))

        if (salB <= 1399.12):
            valorINSS = salB * 0.08
            somaINSS += valorINSS
            salL = salB - valorINSS
        
        elif (salB <= 2331.88):
            valorINSS = salB * 0.09
            somaINSS += valorINSS
            salL = salB - valorINSS
        elif (salB <= 4663.75):
            valorINSS = salB * 0.11
            somaINSS += valorINSS
            salL = salB - valorINSS
        else:
            valorINSS = 513.01
            somaINSS += valorINSS
            salL = salB - valorINSS

        if (dep >=1 ):
            salIR = salL - (dep * 189.59)
            if (salIR <= 1903.98):
                valorIR = 0
                somaIR = somaIR + valorIR
            elif (salIR <= 2826.65):
                valorIR = ((salIR * 0.075)-142.8)
                somaIR = somaIR + valorIR
            elif (salIR <= 3751.05):
                valorIR = ((salIR * 0.15)-354.8);
                somaIR = somaIR + valorIR
            elif(salIR <= 4664.68):
                valorIR = ((salIR * 0.225)-636.13);
                somaIR = somaIR + valorIR            
            else:
                valorIR = ((salIR * 0.275)-869.36);
                somaIR = somaIR + valorIR
        else:
            salIR = salL
            if (salIR <= 1903.98):
                valorIR = 0
                somaIR = somaIR + valorIR
            elif (salIR <= 2826.65):
                valorIR = ((salIR * 0.075)-142.8)
                somaIR = somaIR + valorIR
            elif (salIR <= 3751.05):
                valorIR = ((salIR * 0.15)-354.8);
                somaIR = somaIR + valorIR
            elif(salIR <= 4664.68):
                valorIR = ((salIR * 0.225)-636.13);
                somaIR = somaIR + valorIR            
            else:
                valorIR = ((salIR * 0.275)-869.36);
                somaIR = somaIR + valorIR
        if (salB <= 1399.12):
            salL = (salL - valorIR)
            print(f"Salario Liquido= {salL}\n");
            print(f"Valor INSS= {valorINSS}\n");
            print(f"Valor IR= {valorIR} \n\n");
        
        elif (salB <= 2331.88):
            salL = (salL - valorIR)
            print(f"Salario Liquido= {salL}\n");
            print(f"Valor INSS= {valorINSS}\n");
            print(f"Valor IR= {valorIR} \n\n");
        elif (salB <= 4663.75):
            salL = (salL - valorIR)
            print(f"Salario Liquido= {salL}\n");
            print(f"Valor INSS= {valorINSS}\n");
            print(f"Valor IR= {valorIR} \n\n");
        else:
            salL = (salL - valorIR)
            print(f"Salario Liquido= {salL}\n");
            print(f"Valor INSS= {valorINSS}\n");
            print(f"Valor IR= {valorIR} \n\n");
    print(f"Funcionário: {cod} \n");
    print(f"Valor no ano a pagar de INSS= {somaINSS} \n");
    print(f"Valor no ano a pagar de IR= {somaIR} \n\n");
    cod = int(input("Digite o código do funcionário: "));
    print("\n");