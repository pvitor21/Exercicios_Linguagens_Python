def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

def verificar_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0

def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in palavra if letra in vogais)

def converter_celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
if __name__ == "__main__":
    num = int(input("Digite um número para calcular o fatorial: "))
    print(f"Fatorial de {num}: {calcular_fatorial(num)}")
    
    num = int(input("Digite um número para verificar se é primo: "))
    print(f"{num} é primo? {verificar_primo(num)}")
    
    lista = list(map(float, input("Digite uma lista de números separados por espaço: ").split()))
    print(f"Média da lista: {calcular_media(lista)}")
    
    palavra = input("Digite uma palavra para contar as vogais: ")
    print(f"Número de vogais em '{palavra}': {contar_vogais(palavra)}")
    
    temp_celsius = float(input("Digite a temperatura em Celsius: "))
    print(f"{temp_celsius}°C em Fahrenheit: {converter_celsius_para_fahrenheit(temp_celsius)}°F")
