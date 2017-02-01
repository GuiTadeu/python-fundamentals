# O Python tem um gerenciador de Pacotes: PIP
# Quando tem dois pythons: PIP 2; PIP 3
# Python: Não reinvente a Roda ;)
# Vamos usar a biblioteca Requests, mais bonita, usa URL LIB la no fundo (amigavel)
# URL LIB, Sockets, direto com a Rede
# PIP install requests
# Requisição  WEB é entrar num site
# Requisição e Resposta (Request, Response)
# Enviando informações na requisição
# GET - Pegar informações
# POST - Enviar informações
# Status 200: Deu certo
# 404 - Não existe
# 500 - Erro interno do servidor
# Request Header
# Beautiful Soup 4, pip install bs4
# Puts Request

# Mudando o cabecalho
# Passando Dicionario
# Enganando a Requisição
# Referer é de que site eu vim

import requests

cabecalho = {'User-agent': 'Windows 12', 'Referer': 'Google.com'}

# Passando Cookies
meus_cookies = {'Ultima-visita': '12/12/12'}

dados = {'username': 'GUI', 'password': 'ToSuave2016'}

try:
    requisicao = requests.post('https://putsreq.com/vXtQPHtAI5IWoWNp1jY0', headers=cabecalho, cookies=meus_cookies, data=dados)
    print(requisicao.text)
except Exception as e:
    print('Requisição deu erro:', e)

