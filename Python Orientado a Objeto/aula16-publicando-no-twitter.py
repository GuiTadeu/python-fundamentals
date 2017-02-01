import json
import urllib
import oauth2

consumer_key = 'o4MQKS2CQin4Rl4QsCiU7fUVs'
consumer_secret = 'W1z53xXfkw0w2IruS8yhaLt7mtiD9QJcPioj2Iw3tggoBRztUE'

# Token
access_token = '738913391910195205-vDniBpj1YexCw4HMrboKrBf41ExGPbk'
access_token_secret = 'pu9CGUnRpTed3xz8fIT8gyhoZSWScZMybwhM8ScdNhJnj'

# Perceba como as coisas se encaixam feito peças de Lego:
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(access_token, access_token_secret)
cliente = oauth2.Client(consumer, token)

twittar = input('O que você está pensando?: ')
twittar_codificada = urllib.parse.quote(twittar, safe='')
# O padrão aqui está Get, precisa ser POST
requisicao_twittar = cliente.request("https://api.twitter.com/1.1/statuses/update.json?status="+twittar_codificada, method='POST')
twittar_decodificar = requisicao_twittar[1].decode()
twittar_objeto = json.loads(twittar_decodificar)

print(twittar_objeto)