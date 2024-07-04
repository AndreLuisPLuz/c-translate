
mat1 = []
for l in range (1,6,1):
    a = []
    for c in range (1,4,1):
        a.append(int(input(f"informe a posição da linha {l}, e da coluna {c} da matriz: \n")))
    mat1.append(a)
print("\nSegunda Matriz\n")
mat2 = []
for l in range (1,6,1):
    b = []
    for c in range (1,4,1):
        b.append(int(input(f"informe a posição da linha {l}, e da coluna {c} da matriz: \n")))
    mat2.append(a)

matresul = []
for l in range (0,5,1):
    d = []
    for c in range (0,3,1):
        n = mat1[l][c] + mat2[l][c]
        d.append(n)
    matresul.append(d)  

print("SOMA MATRIZ \n")
for l in range (0,5,1):
    for c in range (0,3,1):
        print(matresul[l][c],end=" ")
    print()