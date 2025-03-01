# Exercício 1
num = int(input("Digite um número inteiro positivo: "))
for i in range(1, num + 1):
    print(i)

# Exercício 2
soma = 0
while True:
    num = int(input("Digite um número (negativo para sair): "))
    if num < 0:
        break
    soma += num
print(f"Soma dos números positivos digitados: {soma}")

# Exercício 3
num = int(input("Digite um número inteiro: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Exercício 4
A = int(input("Digite o valor inicial do intervalo: "))
B = int(input("Digite o valor final do intervalo: "))
for i in range(A, B + 1):
    if i % 2 != 0:
        print(i)

# Exercício 5
N = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
fib = [0, 1]
for i in range(2, N):
    fib.append(fib[-1] + fib[-2])
print("Sequência de Fibonacci:", fib[:N])
