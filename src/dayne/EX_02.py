def calcular(n1,n2,p_soma, p_multi):
    p_soma = n1 + n2
    p_multi = n1 * n2
    pi = ''
    if(p_soma % 2 == 0):
        pi = 'P'
        return pi, p_soma , p_multi
    else:
        pi = 'I'
        return pi, p_soma , p_multi 
    
n1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
n2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
soma =0
multi = 0

resp,soma,multi = calcular(n1,n2,soma,multi)

print(f"\nA soma dos 2 números informados é = {soma}.\n")
print(f"A multipicação dos 2 números informados é = {multi}.\n")
print(f"{resp}.\n\n\n")