def par_impar(p_num):
    pi = ""
    if (p_num % 2 == 0):
        pi = "P"
        print("PAR\n")
    else:
        pi = "I"
        print("IMPAR\n")
    return pi

n = int(input("Informe um Número: "))

resp = par_impar(n)

print(f"{resp} \n")