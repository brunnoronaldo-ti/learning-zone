base = float(input("base do triângulo: "))
altura = float(input("altura do triângulo: "))
print()

print("Deseja calcular a área ou o perímetro do triângulo?")
print("Digite 'A' para área ou 'T' para perímetro.")
R = input("qual resposta deseja obter? ").lower()
print()

if R == "a":
    area = (base * altura) / 2
    print("A área do triângulo é:", area)

elif R == "t":
    hipotenusa = (base**2 + altura**2)**0.5
    perimetro = base + altura + hipotenusa
    print("O perímetro do triângulo é:", perimetro)

else:
    print("Resposta inválida. Por favor, escolha 'A' para área ou 'T' para perímetro.")
