print("bem vindo a calculadora!!")
print("menu:")
print("1- soma")
print("2- subtração")
print("3- multiplicação")
print("4- divisão")
print("5- ver histórico de resultados")
print("6- limpar histórico de resultados")
print("7- rever menu")
print("0- sair")

history = []

while True:
    chose = input("escolha uma opção: ")
    match chose:
        case "1":
            a = float(input("insira o primeiro número: "))
            b = float(input("insira o segundo número: "))
            result = a + b
            print(f"resultado: {result}")
            history.append(result)
            print()
        case "2":
            a = float(input("insira o primeiro número: "))  
            b = float(input("insira o segundo número: "))
            result = a - b
            print(f"resultado: {result}")
            history.append(result)
            print()
        case "3":
            a = float(input("insira o primeiro número: "))  
            b = float(input("insira o segundo número: "))
            result = a * b
            print(f"resultado: {result}")
            history.append(result)
            print()
        case "4":
            a = float(input("insira o primeiro número: "))
            b = float(input("insira o segundo número: "))
            if b == 0:
                print("erro: divisão por zero")
                print()
            else:
                result = a / b
                print(f"resultado: {result}")
                history.append(result)
                print()
        case "5":
            for i, r in enumerate(history, 1):
            print(f"{i} → {r}")
            if not history:
                print("nenhum resultado no histórico.")
            print()

        case "6":
            print("tem certeza que deseja limpar o histórico? (s/n)")
            confirm = input().lower()
            if confirm == 's':
                history.clear() 
                print("histórico limpo.")
                print()
            else:
                print("operação cancelada.")
                print()
        case "7":
            print("menu:") 
            print("1- soma")
            print("2- subtração")
            print("3- multiplicação")
            print("4- divisão")
            print("5- ver histórico de resultados")
            print("6- limpar histórico de resultados")
            print("7- rever menu")
            print("0- sair")
        case "0":
            print("saindo da calculadora. até mais!")
            break
        case _:
            print("opção inválida. por favor, escolha uma opção válida.")

    
