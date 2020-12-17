#13) Obtenha, usando requests ou urllib, o conteúdo
# sobre as PyLadies no link http://brasil.pyladies.com/about e:
#A) Conte todas as palavras no corpo da página,
# e indique quais palavras apareceram apenas uma vez.
#B) Conte quantas vezes apareceu a palavra ladies no conteúdo da página.


import requests
import re
from collections import Counter
from bs4 import BeautifulStoneSoup as bss


repeated_words = 0
ladies = 0
words_list = []
only1 = []
request = requests.get('http://brasil.pyladies.com/about')

def starting():

    request.encoding = request.apparent_encoding
    soup = bss(request.text, 'lxml')
    for item in soup.html.body.article.find_all('div'):
        words_list = [re.sub('\W+', '', word).lower() for word in item.text.split()]
    words = len(words_list)
    return words

def data_processing():

    starting()
    word_dict = dict(Counter(words_list))
    ladies = word_dict['ladies']
    for key, value in word_dict.items():
        if value == 1:
            only1.append(key)


data_processing()
print('Temos {} palavras no conteúdo sobre as PyLadies;\n E {} palavras aparecem apenas uma vez,\n',
      'já a palavra ladies se repete {} vezes.\n'.format(words, len(only1), ladies),
      '{} Esta é a lista das palavras que aparecem apenas uma vez no conteúdo:'.format(' '))
for word in only1:
    print(word)