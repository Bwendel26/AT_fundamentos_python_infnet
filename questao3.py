# Usando o Thonny, escreva uma função em Python chamada potencia.
# Esta função deve obter como argumentos dois números inteiros,
# A e B, e calcular AB usando multiplicações sucessivas
# (não use a função de python math.pow) e retornar o resultado
# da operação. Depois, crie um programa em Python que obtenha dois
# números inteiros do usuário e indique o resultado de AB usando a função.

def potencia(number, power):

    result = number
    for i in range(power):
        if i == 0:
            result = number
        else:
            result *= number

    return result


base = int(input("Give a integer number (base): "))
exponent = int(input("Give a integer number (exponent): "))

print(potencia(base, exponent))