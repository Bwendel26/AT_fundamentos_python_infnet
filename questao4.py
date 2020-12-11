# Escreva um programa em Python que leia um vetor de 5 números
# inteiros e o apresente na ordem inversa. Imprima o vetor no final. Use listas.
# Exemplo: se a entrada for [4, 3, 5, 1, 2], o resultado deve ser [2, 1, 5, 3, 4].

def list_invert(vector):

    result = vector[::-1]
    return result

entry_vector = input("Give the numbers of the list: ")
print(list_invert(entry_vector))