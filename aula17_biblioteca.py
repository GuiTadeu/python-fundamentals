import oauth2
import urllib.parse
import json

# Criando Objeto do tipo Twitter
class Twitter:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.conexao(consumer_key, consumer_secret, token_key, token_secret)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):

        # Atributos do objeto
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)



    def tweet(self, novo_tweet):
        twittar_codificada = urllib.parse.quote(novo_tweet, safe='')
        requisicao_twittar = self.cliente.request(
            "https://api.twitter.com/1.1/statuses/update.json?status=" + twittar_codificada, method='POST')
        twittar_decodificar = requisicao_twittar[1].decode()
        twittar_objeto = json.loads(twittar_decodificar)


