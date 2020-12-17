#11) OBTENHA, USANDO REQUESTS OU URLLIB, DENTRO DE SEU PROGRAMA EM PYTHON, O CSV DO LINK:
#HTTPS://SITES.GOOGLE.COM/SITE/DR2FUNDAMENTOSPYTHON/ARQUIVOS/VIDEO_GAMES_SALES_AS_AT_22_DEC_2016.CSV

#OBTENHA, DENTRE OS JOGOS DO GÊNERO DE AÇÃO (ACTION), TIRO (SHOOTER) E PLATAFORMA (PLATFORM):

# 1 QUAIS SÃO AS TRÊS MARCAS QUE MAIS PUBLICARAM JOGOS DOS
# TRÊS GÊNEROS COMBINADOS? INDIQUE TAMBÉM O TOTAL DE JOGOS DE CADA MARCA.

# 2 QUAIS SÃO AS TRÊS MARCAS QUE MAIS VENDERAM OS TRÊS GÊNEROS
# COMBINADOS? INDIQUE TAMBÉM O TOTAL DE VENDAS DE CADA MARCA.

# 3 QUAL É A MARCA COM MAIS PUBLICAÇÕES EM CADA UM DOS GÊNEROS
# NOS ÚLTIMOS DEZ ANOS NO JAPÃO? INDIQUE TAMBÉM O NÚMERO TOTAL DE JOGOS DELA.

# 4 QUAL FOI A MARCA QUE MAIS VENDEU EM CADA UM DESSES GÊNEROS
# NOS ÚLTIMOS DEZ ANOS, NO JAPÃO? INDIQUE TAMBÉM O TOTAL DE VENDAS DELA.


import pandas as pd

url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv'
dataframe = pd.read_csv(url, sep=',')


game_genre = dataframe[(dataframe['Genre'] == 'Action') | (
    dataframe['Genre'] == 'Shooter') | (dataframe['Genre'] == 'Platform')]
biggest_sellers = dataframe.groupby(
    ['Publisher'])['Global_Sales'].sum().sort_values(ascending=False)
japan_action = dataframe[(dataframe['Year_of_Release'] >= 2010) & (
    dataframe['Genre'] == 'Action')]
japan_shooter = dataframe[(dataframe['Year_of_Release'] >= 2010) & (
    dataframe['Genre'] == 'Shooter')]
japan_platform = dataframe[(dataframe['Year_of_Release'] >= 2010) & (
    dataframe['Genre'] == 'Platform')]
sales_japan_action = dataframe[(
    dataframe['Year_of_Release'] >= 2010) & (dataframe['Genre'] == 'Action')]
sales_japan_shooter = dataframe[(
    dataframe['Year_of_Release'] >= 2010) & (dataframe['Genre'] == 'Shooter')]
sales_japan_platform = dataframe[(
    dataframe['Year_of_Release'] >= 2010) & (dataframe['Genre'] == 'Platform')]


game_genre_report = game_genre.groupby(
    ['Publisher'])['Publisher'].count().sort_values(ascending=False).head(3)

biggest_sellers_report = biggest_sellers.head(3)

ja_publisher = japan_action.groupby(
    ['Publisher'])['Publisher'].count().sort_values(ascending=False)

js_publisher = japan_shooter.groupby(
    ['Publisher'])['Publisher'].count().sort_values(ascending=False)

jp_publisher = japan_platform.groupby(
    ['Publisher'])['Publisher'].count().sort_values(ascending=False)

ja_seller = sales_japan_action.groupby(
    ['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

js_seller = sales_japan_shooter.groupby(
    ['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

jp_seller = sales_japan_platform.groupby(
    ['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)


print(
    'Informações sobre jogos do gênero de ação (Action), tiro (Shooter) e \nplataforma (Platform)',
    'Marcas que mais publicaram jogos:\n{}'.format(
        game_genre_report),
    '---' * 25,
    'Três maiores vendedores de jogos:\n{}'.format(
        biggest_sellers_report),
    '---' * 25,
    'Marca com mais publicações no gênero action:\n{}'.format(
        ja_publisher.head(1)),
    '---' * 25,
    'Marca com mais publicações no gênero shooter:\n{}'.format(
        js_publisher.head(1)),
    '---' * 25,
    'Marca com mais publicações no gênero platform:\n{}'.format(
        jp_publisher.head(1)),
    '---' * 25,
    'Marca que mais vendeu no gênero action nos ultimos 10 anos:\n{}'.format(
        ja_seller.head(1)),
    '---' * 25,
    'Marca que mais vendeu no gênero shooter nos ultimos 10 anos:\n{}'.format(
        js_seller.head(1)),
    '---' * 25,
    'Marca que mais vendeu no gênero platform nos ultimos 10 anos:\n{}'.format(
        jp_seller.head(1)),
    '---' * 25, sep="\n")