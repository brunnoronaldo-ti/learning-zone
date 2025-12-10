print("Digite dois números inteiros diferentes:")
print("o progrmama continuará pedindo até que os números sejam iguais.")
x = int(input("Primeiro número: "))
y = int(input("Segundo número: "))

while x != y:
    if x < y:
        print("crescente!")
        x = int(input("Primeiro número: "))
        y = int(input("Segundo número: "))
    elif x > y:
        print("decrescente!")
        x = int(input("Primeiro número: "))
        y = int(input("Segundo número: "))
    
    
print("números iguais. fim do programa.")
