a = int(input("digite o primeiro número: "))
b = int(input("digite o segundo número: "))
c = int(input("digite o terceiro número: "))

menor = min(a, b, c)
maior = max(a, b, c)
media = (a + b + c) / 3
diferenca = maior - menor

print()
print("os números digitados foram:", a, b, c)
print("o menor número é:", menor)
print("o maior número é:", maior)
print("a diferença entre eles é:", diferenca)
print("a média é:", media)
#um programa feito para calcular o maior, o menor e a média de três números fornecidos pelo usuário
#feito para treinar estruturas condicionais e operações matemáticas básicas
