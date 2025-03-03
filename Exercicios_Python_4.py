# Exercicio 1
def soma_lista():
    lista = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))
    print("Soma dos elementos:", sum(lista))

# Exercicio 2
def maior_menor():
    lista = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))
    print(f"Maior número: {max(lista)}, Menor número: {min(lista)}")

# Exercicio 3
def remover_duplicatas():
    lista = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))
    lista_sem_duplicatas = list(dict.fromkeys(lista))
    print("Lista sem duplicatas:", lista_sem_duplicatas)

# Exercicio 4
def inverter_lista():
    lista = input("Digite uma lista de palavras separadas por espaço: ").split()
    print("Lista invertida:", list(reversed(lista)))

# Exercicio 5
def contar_ocorrencias():
    lista = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))
    numero = int(input("Digite o número que deseja contar: "))
    print(f"O número {numero} aparece {lista.count(numero)} vezes na lista.")

soma_lista()
maior_menor()
remover_duplicatas()
inverter_lista()
contar_ocorrencias()
