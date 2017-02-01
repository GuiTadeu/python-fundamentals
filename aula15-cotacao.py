import requests
import json

requisicao_cotacao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
cotacao = json.loads(requisicao_cotacao.text)
print('A cotação atual do Dólar está:', cotacao['valores']['USD']['valor'])

requisicao_tempo = requests.get('https://api.hgbrasil.com/weather/?format=json&cid=BRXX0198')
print(requisicao_tempo)
