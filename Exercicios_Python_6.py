# Exercicio 1
produto = ("Notebook", 3500.00, 10)
print(f"Produto: {produto[0]}\nPreço: R${produto[1]:.2f}\nQuantidade em estoque: {produto[2]}")

# Exercicio 2
numeros = tuple(int(input(f"Digite o {i+1}º número: ")) for i in range(4))
print(f"O número 9 apareceu {numeros.count(9)} vezes.")
if 3 in numeros:
    print(f"O primeiro número 3 apareceu na posição {numeros.index(3) + 1}.")
else:
    print("O número 3 não foi digitado.")
print(f"Números pares: {[n for n in numeros if n % 2 == 0]}")

# Exercicio 3
cores_arco_iris = ("Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta")
pos = int(input("Digite um número de 1 a 7 para ver a cor correspondente: "))
if 1 <= pos <= 7:
    print(f"A cor correspondente é {cores_arco_iris[pos-1]}.")
else:
    print("Número inválido.")

# Exercicio 4
alunos = ("Ana", 8.5, "Carlos", 7.0, "Beatriz", 9.2, "Daniel", 6.8, "Eduarda", 8.0)
nomes = alunos[0::2]
notas = alunos[1::2]
print(f"Nomes dos alunos: {nomes}")
print(f"Notas dos alunos: {notas}")

# Exercicio 5
times = ("Flamengo", "Palmeiras", "Atlético-MG", "São Paulo", "Corinthians", "Internacional", "Grêmio", "Fluminense", "Botafogo", "Santos")
print(f"Os três primeiros colocados: {times[:3]}")
print(f"Os últimos três colocados: {times[-3:]}")
print(f"Times em ordem alfabética: {sorted(times)}")
time = input("Digite o nome de um time para saber sua posição: ")
if time in times:
    print(f"O {time} está na posição {times.index(time) + 1}.")
else:
    print("Time não encontrado na lista.")
