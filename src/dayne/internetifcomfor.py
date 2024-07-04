alt_mulheres = 0
_mulheres = 0
_homens = 0

for i in range(1,3,1):
    sx = int(input("Digite o genero\nUse 0 - Feminino e 1 - Masculino:\n"))

    alt= float(input("Informe a Altura\n"))

    if(i==1):
        maior=alt
        menor=alt

    if(alt>maior):
        maior=alt

    if(alt<menor):
        menor=alt
    
    if(sx == 0):
        alt_mulheres += alt
        _mulheres += 1
    else:
        _homens += 0
if(_mulheres > 0):
    media_mulher = alt_mulheres/_mulheres
    print(f"\n\nMedia -> Mulheres: {media_mulher:.2f} ")
else:
    print("\nNenhuma mulher inserida para obter uma media!")
print(f"\nQuantidade-> Homens:{_homens} ")
print(f"\n{menor: .2f} Menor Altura e Maior Altura {maior: .2f}\n")