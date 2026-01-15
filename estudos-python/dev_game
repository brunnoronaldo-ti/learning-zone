import random

#jogo RPG no terminal

vida = 100
sanidade = 100
projeto_porcentagem = 0

bugs_encontrados = [
    "Bug de sintaxe",
    "Bug de lógica",
    "Bug de desempenho",
    "Bug de segurança",
    "Bug de compatibilidade"
]

jogos = [
    "jogo da forca",
    "jogo da adivinhação",
    "minecraft",
    "among us",
    "roblox"
]

print("---------------------------------------------------")
print("você acordou dentro do terminal do seu computador.")
print("você precisa entregar seu projeto, mas encontrou alguns bugs no código.")
print("Cada bug que você resolve aumenta a porcentagem do projeto em 20%")
print("tome decisões com cuidado e boa sorte!")
print("---------------------------------------------------")

while vida > 0 and sanidade > 0 and projeto_porcentagem < 100:
    print("----------------------------------------------------")
    print(f"\nVida: {vida}, Sanidade: {sanidade}, Projeto: {projeto_porcentagem}%")
    print("----------------------------------------------------")
    print("")
    bug = random.choice(bugs_encontrados)
    print(f"Você encontrou um {bug}!")
    print("O que você quer fazer?")
    print("1. Tentar resolver o bug ")
    print("2. Ignorar o bug ")
    print("3. Pedir ajuda")
    print("4. Jogar um jogo para relaxar ")
    escolha = input("Escolha uma opção (1-4): ")
    print("")

    if escolha == "1":
        sucesso = random.choice([True, False])
        if sucesso:
            print(f"Você resolveu o {bug}!")
            projeto_porcentagem += 10
            sanidade -= 5
        else:
            print(f"Você não conseguiu resolver o {bug} e tudo quebrou!")
            vida -= 30
            sanidade -= 20           
    elif escolha == "2":
        print(f"Você ignorou o {bug}, mas perdeu 15 de vida, mas ganhou 5 de sanidade.")
        vida -= 15
        sanidade += 5
    elif escolha == "3":
        print("Você pediu ajuda e perdeu 10 de sanidade, mas conseguiu resolver o bug.")
        projeto_porcentagem += 10
        sanidade -= 10
    elif escolha == "4":
        print("Você decidiu jogar um jogo para relaxar.")
        print(f"Vamos jogar {random.choice(jogos)}!")
        vida += 5
        sanidade += 5
        print("Você se sentiu mais relaxado.")
    else:
        print("Opção inválida, o terminal não perdoa.")
        print("Você perdeu 15 de vida por erro de sintaxe.")
        vida -= 15

if projeto_porcentagem >= 100:
    print("Parabéns! Você entregou o projeto a tempo e salvou o dia!")
    print("Você venceu o jogo! 🎉")
elif vida <= 0:
    print("Você ficou sem vida e o terminal te engoliu. Game Over!")
elif sanidade <= 0:
    print("Sua sanidade acabou e você entrou em burnout. Game Over!")
