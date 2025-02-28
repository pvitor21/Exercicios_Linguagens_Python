# 1 Exercicio
import math

raio = float(input("Digite o raio do circulo: "))
area = math.pi * raio ** 2
print(f"A área do circulo é: {area:.2f}")

# 2 Exercicio

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")

#3 Exercicio

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))

media = (n1 + n2 + n3) / 3
print(f"A média dos tres números é: {media:.2f}")

# 4 Exercicio

horas_trabalhadas = float(input("Digite o numero de horas trabalhadas no mês: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))

salario_total = horas_trabalhadas * valor_por_hora
print(f"O salário total do mês é: R${salario_total:.2f}")

# 5 Exercicio

metros = float(input("Digite um valor em metros: "))
centimetros = metros * 100
print(f"O valor em centímetros é: {centimetros:.2f} cm")


