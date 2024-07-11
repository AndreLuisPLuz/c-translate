print("PRIMEIRA MATRIZ \n")
matrix1 = []
for l in range (0,3,1):
    a = []
    for c in range (0,3,1):
        a.append(int(input("Add um numero:")))
    matrix1.append(a)  

print("SEGUNDA MATRIZ \n")
matrix2 = []
for l in range (0,3,1):
    b = []
    for c in range (0,3,1):
        b.append(int(input("Add um numero:")))
    matrix2.append(b)  

matrixSoma = []
for l in range (0,3,1):
    d = []
    for c in range (0,3,1):
        n = matrix1[l][c] + matrix2[l][c]
        d.append(n)
    matrixSoma.append(d)  

print("SOMA MATRIZ \n")
for l in range (0,3,1):
    for c in range (0,3,1):
        print(matrixSoma[l][c],end=" ")
    print()