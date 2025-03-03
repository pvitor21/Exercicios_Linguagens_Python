# Exercicio 1
alunos = {}
for _ in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota
print("Lista de alunos e suas notas:", alunos)

# Exercicio 2
palavra = input("Digite uma palavra: ")
contagem = {}
for letra in palavra:
    contagem[letra] = contagem.get(letra, 0) + 1
print("Contagem de caracteres:", contagem)

# Exercicio 3
traducao = {"casa": "house", "gato": "cat", "cachorro": "dog", "livro": "book", "mesa": "table"}
termo = input("Digite uma palavra em português para traduzir: ")
print(traducao.get(termo, "Tradução não encontrada."))

# Exercicio 4
frase = input("Digite uma frase: ")
palavras = frase.split()
contagem_palavras = {}
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print("Contagem de palavras:", contagem_palavras)

# Exercicio 5
catalogo = {
    "001": ("Notebook", 3500.00),
    "002": ("Mouse", 150.00),
    "003": ("Teclado", 200.00),
    "004": ("Monitor", 1200.00),
    "005": ("Impressora", 800.00)
}
codigo = input("Digite o código do produto: ")
produto = catalogo.get(codigo, "Produto não encontrado.")
print(produto)
