conttotal = 0;
contIA = 0;
contIB = 0;
contJA = 0;
contJB = 0;
contADUL = 0;

idade = int(input("Qual a idade do nadador? \n"));

while(idade > 0):
    if(idade >= 18):
        contADUL += 1;
        conttotal += 1;
        print("ADULTO \n");
    else:
        if(idade >= 8 and idade <= 10):
            contJA += 1;
            conttotal += 1;
            print("Juveil A \n");
        else:
            if(idade >= 14 and idade<=17):
                contJB += 1;
                conttotal += 1;
                print("Juvenil B \n");
    idade = int(input("Qual a idade do nadador? \n"));
print(f" Categoria infantil A sao: {contIA} \n");
print(f" Categoria infantil B sao: {contIA} \n");
print(f" Categoria juvenil A sao: {contJA} \n");
print(f" Categoria juvenil B sao: {contJB} \n");
print(f" Categoria Adultos sao: {contADUL} \n\n");

print(f"total: {conttotal} \n");
