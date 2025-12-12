print("Bem vindo!!")
print("Esse programa guarda as notas de alunos e calcula a média de cada um")

# Inicializar lista para armazenar os alunos com suas notas e médias
alunos = []

# Validar entrada de num_alunos
while True:
    try:
        num_alunos = int(input("Insira quantos alunos serão digitados: "))
        if num_alunos > 0:
            break
        else:
            print("Número deve ser maior que 0.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Loop para cada aluno
#testei diversos loops até chegar nesse que me parece mais simples
for i in range(num_alunos):
    # Coletar nome (simples, sem validação extra além de não vazio)
    nome = input(f"Digite o nome do aluno {i+1}: ").strip()
    while not nome:
        print("Nome não pode ser vazio.")
        nome = input(f"Digite o nome do aluno {i+1}: ").strip()

    notas_aluno = []
    for j in range(4):
        while True:
            try:
                nota = float(input(f"Digite a nota {j+1} do aluno {nome} (entre 0 e 10): "))
                if 0 <= nota <= 10:
                    notas_aluno.append(nota)
                    break
                else:
                    print("Nota inválida. Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    # Calcular a média do aluno
    media = sum(notas_aluno) / len(notas_aluno)
    alunos.append({'nome': nome, 'notas': notas_aluno, 'media': media})

print("\n--- Resultados ---")

# Exibir as notas e média de cada aluno
for aluno in alunos:
    print(f"Notas do aluno {aluno['nome']}: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")
    if aluno['media'] >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    print()

print("Fim do programa")
