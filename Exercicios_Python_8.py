#Exercicio 1
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print("Resultado da divisão:", resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")

#Exercicio 2
try:
    nome_arquivo = input("Digite o nome do arquivo: ")
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:", conteudo)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")

#Exercicio 3
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print("O dobro do número é:", numero * 2)
        break
    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro válido.")

#Exercicio 4
numeros = [10, 20, 30, 40, 50]
try:
    indice = int(input("Digite um índice (0 a 4): "))
    print("Elemento na posição", indice, "é", numeros[indice])
except IndexError:
    print("Erro: Índice fora do intervalo válido.")
except ValueError:
    print("Erro: Entrada inválida. Digite um número inteiro.")

#Exercicio 5
class SaldoInsuficienteError(Exception):
    pass

saldo = 1000.00
try:
    saque = float(input("Digite o valor do saque: "))
    if saque > saldo:
        raise SaldoInsuficienteError("Erro: Saldo insuficiente para saque.")
    saldo -= saque
    print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
except ValueError:
    print("Erro: Entrada inválida. Digite um valor numérico.")
except SaldoInsuficienteError as e:
    print(e)
