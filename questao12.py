#12-B) ESCREVA UM PROGRAMA QUE OBTENHA DO USUÁRIO UMA SIGLA
# DO ESTADO DA REGIÃO CENTRO-OESTE E APRESENTA SUAS INFORMAÇÕES CORRESPONDENTES NA TABELA.
# O RESULTADO DEVE APRESENTAR APENAS O CONTEÚDO, SEM FORMATAÇÃO.
# OU SEJA, AS TAGS NÃO DEVEM APARECER. NÃO ESQUEÇA DE CHECAR SE A SIGLA PERTENCE À REGIÃO.

import requests
from bs4 import BeautifulSoup



request = requests.get(
    'https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html')
states = ['df', 'mt', 'go', 'ms']
data = ''
user_choice = ''

request.encoding = request.apparent_encoding
bs = BeautifulSoup(request.text, "lxml")
table = bs.html.body.find('div', {'class': 'tabela'})
lines = bs.html.body.article.find_all('div', {'class': 'linha'})

stop = False
while not stop:
    data = input("Informe a sigla de um estado do Centro Oeste: ")
    for line in lines:
        _state = line.find_all('div', {'class': 'celula'})[0].text
        if data == _state.lower():
            usr_choice = line.text
            stop = True

print('Conteúdo da tabela:\n {} '.format(table.get_text()))
print(user_choice)