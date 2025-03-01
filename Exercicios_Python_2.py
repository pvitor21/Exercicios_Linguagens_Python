# Exercício 1
"""num = int(input("Digite um numero inteiro: "))
if num % 2 == 0:
    print("O numero é par.")
else:
    print("O numero é impar.")

# Exercício 2
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
if num1 > num2:
    print(f"O maior numero é {num1}.")
elif num2 > num1:
    print(f"O maior número é {num2}.")
else:
    print("Os numeros são iguais.")

# Exercício 3
idade = int(input("Digite a idade: "))
if idade < 18:
    print("Menor de idade.")
elif 18 <= idade < 60:
    print("Adulto.")
else:
    print("Idoso.")


# Exercício 4
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Aprovado.")
elif 5 <= media < 7:
    print("Recuperação.")
else:
    print("Reprovado.")"""

# Exercício 5
lado1 = int(input("Digite o primeiro lado do triângulo: "))
lado2 = int(input("Digite o segundo lado do triângulo: "))
lado3 = int(input("Digite o terceiro lado do triângulo: "))
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os lados formam um triângulo válido.")
else:
    print("Os lados não formam um triângulo válido.")