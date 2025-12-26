def jogo_da_forca():
    import random

    print("================ JOGO DA ADIVINHAÇÃO ================")

    estagios = [
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =======
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =======
    """,
    """
    +---+
     |  |
     O  |
    /|  |
        |
        |
    =======
    """,
    """
    +---+
     |  |
     O  |
    /|\ |
        |
        |
    =======
    """,
    """
    +---+
     |  |
     O  |
    /|\ |
    /   |
        |
    =======
    """,
    """
    +---+
     |  |
     O  |
    /|\ |
    / \ |
        |
    =======
    """
    ]
    #essa lista "estagios" contém as diferentes fases do boneco da forca

    palavra = [
        "python",
        "java",
        "javascript",
        "ruby",
        "html",
        "css",
        "react",
        "angular",
        "node",
        "django",
        ]

    palavra_secreta = random.choice(palavra)
    palavra_oculta = ["*"] * len(palavra_secreta)
    #"ramdom.choice(palavra)" escolhe uma palavra aleatória da lista "palavra"
    #"palavra_oculta" cria uma lista com asteriscos do mesmo tamanho da palavra secreta

    tentativas = 6
    letras_usadas = []

    while tentativas > 0 and "*" in palavra_oculta:
        print("\nPalavra:", "".join(palavra_oculta))
        print("Tentativas restantes:", tentativas)
        print("Letras usadas:", ", ".join(letras_usadas))

        letra = input("Chute uma letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, insira apenas uma letra.")
            continue
        if letra in letras_usadas:
            print("Você já usou essa letra. Tente outra.")
            continue
        letras_usadas.append(letra)

        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    palavra_oculta[i] = letra
        else:
            print()
            print("Letra errada…")
            print(estagios[6 - tentativas])
            tentativas -= 1

        if "*" not in palavra_oculta:
            print()
            print("\n🎉 Você venceu!")
            print("A palavra era:", palavra_secreta)
        elif tentativas == 0:
            print()
            print("\n💀 Você perdeu!")
            print("A palavra era:", palavra_secreta)

    print("=============== FIM DO JOGO ===============")

while True:
    jogo_da_forca()

    resposta = input("\nQuer jogar novamente? (s/n): ").lower()
    if resposta != "s":
        print("Valeu por jogar. Até a próxima 👋")
        break
