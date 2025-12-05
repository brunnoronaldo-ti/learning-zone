m = int(input("Digite o número de linhas da matriz: "))
n = int(input("Digite o número de colunas da matriz: "))

matriz: [[int]] = [[0 for x in range (n)] for x in range (m)]

for i in range (0, m):
    for j in range (0, n):
        matriz[i][j] = int(input(f"Digite o elemento da posição [{i}][{j}]: "))

print()
print("Matriz digitada:")

for i in range (0, m):
    for j in range (0, n):
        print(matriz[i][j], end=" ")
    print() 
