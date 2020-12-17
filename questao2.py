# Usando o Thonny, escreva um programa em Python que
# some todos os números pares de 1 até um dado n, inclusive.
# O dado n deve ser obtido do usuário. No final, escreva
# o valor do resultado desta soma.

def sum_nums(n):

    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum += i
        else:
            pass

    return sum

user_input = int(input("Give a integer number: "))

print(sum_nums(user_input))