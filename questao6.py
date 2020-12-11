#6) Escreva uma função em Python que:
#leia uma tupla contendo números inteiros,
#retorne uma lista contendo somente os números ímpares
#e uma nova tupla contendo somente os elementos nas posições pares.

def le_tupla(tupla):
    return tupla

def mostra_inteiro(tupla):
    return [n for n in tupla if n % 2 != 0]

def mostra_p(tupla):
    return tuple(n for n in tupla if n % 2 == 0)

def mostra_index(tupla):
    return tuple(n for i, n in enumerate(tupla) if i % 2 == 0)


tupla = (1, 2, 3, 57, 47, 33, 127, 264, 555, 55, 7, 9)

l_i = mostra_inteiro(tupla)
tup_p = mostra_p(tupla)
s_index = mostra_index(tupla)

print(f"Tupla: {le_tupla(tupla)}")
print(f"Lista de ímpares: {mostra_inteiro(tupla)}")
print(f"Tupla de pares: {mostra_p(tupla)}")
print(f"Tupla com elementos em posições pares: {mostra_index(tupla)}")