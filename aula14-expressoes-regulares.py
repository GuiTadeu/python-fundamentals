# REGEX
import re
import requests

requisicao = requests.get('http://lacoxinha.com.br/contato')
string_de_teste_search = "O Gato é zica"
string_de_teste_findall = "O gato, a gata, os gatinhos, os gatos"
pegar_email = "gtadeu@bol.com " \
              "zicadabalada " \
              "josod gui@gmail.com " \
              "djdjakse"
# O r transforma o texto em RAW String
# RAW String pega os caracteres especiais e tira
# Tira os "Enter"
# Colocamos o r para o caracter especial  deixar de ser especial
# O ponto equivale a qualquer caracter r'Gat.'
# O \W coloca letras, não considera espaço vazio
# \W \W \W \W procura qual palavra tem quatro letras
# Depois do Gat pode ter uma ou mais letras
# Repete o padrão
# O asterisco pode ter 0 ou mais
# \. é para ver se tem um ponto


padrao_search = re.search(r'Gat\w', string_de_teste_search)
padrao_findall = re.findall(r'gat\w+', string_de_teste_findall)
padrao_email = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', pegar_email)

# Não se esquecer de converter a requisição para texto!
# requisicao.text
padrao_email_requests = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)

if padrao_search:
    print(padrao_search.group())
else:
    print('Padrão não encontrado')

if padrao_findall:
    print(padrao_findall)
else:
    print('Padrão não encontrado')

if padrao_email:
    print(padrao_email)
else:
    print('Padrão não reconhecido')

if padrao_email_requests:
    print(padrao_email_requests)
else:
    print('Padrão não reconhecido')

