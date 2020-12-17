#10) OBTENHA, USANDO REQUESTS OU URLLIB, DENTRO DE SEU PROGRAMA EM PYTHON, O CSV DO LINK:
#HTTPS://SITES.GOOGLE.COM/SITE/DR2FUNDAMENTOSPYTHON/ARQUIVOS/WINTER_OLYMPICS_MEDALS.CSV
#E:
#DENTRE OS SEGUINTES PAÍSES NÓRDICOS: SUÉCIA, DINAMARCA E NORUEGA,
# VERIFIQUE: NO SÉCULO XXI (A PARTIR DE 2001), QUAL FOI O MAIOR MEDALHISTA
# DE OURO, CONSIDERANDO APENAS AS SEGUINTES MODALIDADES:
#CURLING
#PATINAÇÃO NO GELO (SKATING)
#ESQUI (SKIING)
#HÓQUEI SOBRE O GELO (ICE HOCKEY)
#PARA CADA ESPORTE, CONSIDERE TODAS AS MODALIDADES, TANTO NO MASCULINO QUANTO
# NO FEMININO. SUA RESPOSTA DEVE IMPRIMIR UM RELATÓRIO MOSTRANDO O TOTAL DE
# MEDALHAS DE CADA UM DOS PAÍSES E EM QUE ESPORTE, ANO, CIDADE E GÊNERO
# (MASCULINO OU FEMININO) CADA MEDALHA FOI OBTIDA.

import requests
# import csv

url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv'
gold_medals = []
total_medals = {}

csv = requests.get(url).text
csv_lines = csv.splitlines()

for line in csv_lines:
    coluna = line.split(',')
    if coluna[0] != 'Year' and int(coluna[0]) >= 2001:
        if coluna[4] == 'SWE' or coluna[4] == 'DEN' or coluna[4] == 'NOR':
            if coluna[2] == 'Curling' or coluna[2] == 'Skating' or coluna[2] == 'Skiing' or coluna[2] == 'Ice Hockey':
                if coluna[7] == 'Gold':
                    gold_medals.append(coluna)


country_gold_medal = {'SWE': 0, 'DEN': 0, 'NOR': 0}
for country in gold_medals:
    if country[4] == 'SWE':
        country_gold_medal['SWE'] += 1
    if country[4] == 'DEN':
        country_gold_medal['DEN'] += 1
    if country[4] == 'NOR':
        country_gold_medal['NOR'] += 1

    total_medals = country_gold_medal

print(total_medals)