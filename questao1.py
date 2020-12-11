# Usando o Thonny, escreva um programa em Python que leia uma tupla
# contendo 3 números inteiros, (n1, n2, n3) e os imprima em ordem crescente.

def read_tups(tup):

    #     Implementar codigo proprietario...
    return tuple(sorted(tup))


tupla = (3, 2, 1)
print(read_tups(tupla))