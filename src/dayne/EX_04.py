def conta(x):
    if(x <= 100):
        print(f"{x} \n")
        conta(x + 1)
num = int(input("Indorme um número para ir dele até 100: "))
conta(num)