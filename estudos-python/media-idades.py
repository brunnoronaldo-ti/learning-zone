print("!!bem vindo!!")
print("esse programa calcula a média das idades de um grupo de pessoas")
gp = int(input("quantas pessoas tem no grupo?"))

if gp <= 0:
    print("O número de pessoas deve ser maior que zero.")
    exit()

# Inicializamos uma lista vazia para armazenar as idades
vet = []
soma = 0

for i in range(gp): # Loop para coletar as idades
    while True:
        try:
            idade = int(input(f"insira a idade da pessoa {i + 1}: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue

        if idade <= 0:
            print("Idade deve ser maior que zero. Tente novamente.")
            continue

        break

    vet.append(idade)  # Adiciona a idade ao vetor
    soma = soma + idade
    
media = soma / gp
print(f"a média das idades é: {media:.1f}")
print("as idades são:", vet)

# Alternativamente, podemos usar a função sum() para calcular a soma
# soma = sum(vet)
