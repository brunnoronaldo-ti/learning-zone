#um programa feito para calcular o maior, o menor e a média de três números fornecidos pelo usuário
#feito para treinar estruturas condicionais e operações matemáticas básicas
a = int(input("digite o primeiro número: "))
b = int(input("digite o segundo número: "))
c = int(input("digite o terceiro número: "))

if a <= b and a <= c:
    menor = a
elif b <= a and b <= c:
    menor = b
elif c <= a and c <= b:
    menor = c
else:
    menor = None  # Caso improvável, mas para garantir que a variável seja definida

if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
elif c >= a and c >= b:
    maior = c
else:
    maior = None  #idem

print()
print("os números digitados foram:", a, ",", b, "e", c)
print("o menor número é:", menor)
print("o maior número é:", maior)
if menor is not None and maior is not None:
    diferenca = maior - menor
    print("a diferença entre o maior e o menor número é:", diferenca)
else:
    print("Não foi possível determinar o menor ou maior número.")

media = (a + b + c) / 3
print("a média dos três números é:", media)
