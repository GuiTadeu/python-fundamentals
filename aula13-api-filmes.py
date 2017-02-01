import requests

# A Biblioteca JSON transforma o arquivo em objeto Dict Python
import json

# Criando a Função para retornar dados do filme através do titulo
def requisicao(titulo):
    try:
        # Dando um Get na pagina e passando como Title o Titulo da função
        requisicao = requests.get('http://www.omdbapi.com/?t=' + titulo + '&type=movie')
        # Transformando o arquivo JSON em Dicionario Python
        dicionario = json.loads(requisicao.text)
        # Retornando o Dicionario
        return dicionario
    except Exception as erro:
        print('Deu erro na conexão:', erro)
    return None

def printar_detalhes(filme):

    print('\nTitulo:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota IMDB:', filme['imdbRating'])
    print('Premios:', filme['Awards'])
    print('Poster:', filme['Poster'])


# Enquanto o sair estiver falso ele vai rodar o programa
sair = False
while not sair:
    op = input('\nEscreva o nome de um filme ou SAIR para fechar: ')
    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            printar_detalhes(filme)


