#6) Escreva uma função em Python que:
#leia uma tupla contendo números inteiros,
#retorne uma lista contendo somente os números ímpares
#e uma nova tupla contendo somente os elementos nas posições pares.

def read_tup(tup):

    odd_list = []
    position_even = []
    for i in range(len(tup)):
        if tup[i] % 2 != 0:
            odd_list.append(tup[i])

        if i == 0 or i % 2 == 0:
            position_even.append(tup[i])

    tup_position_even = tuple(position_even)

    return odd_list, tup_position_even


#ERROR TO INSERT NUMBERS
entry = 0
entry_list = []
counter = 1
print("Please insert a element (integer number) \nin the tuple or insert nothing to stop:\n")
while type(entry) == int:

    if type(entry) == int:
        entry = input("Number {}: ".format(counter))
        entry_list.append(entry)
        counter += 1
    else:
        pass


entry_tup = tuple(entry_list)
read_tup_list = read_tup(entry_tup)
print("This is the list with the odd numbers: {}".format(read_tup_list[0]))
print("This is the tuple with even position numbers: {}".format(read_tup_list[1]))