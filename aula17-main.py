from aula17_biblioteca import Twitter

consumer_key = 'o4MQKS2CQin4Rl4QsCiU7fUVs'
consumer_secret = 'W1z53xXfkw0w2IruS8yhaLt7mtiD9QJcPioj2Iw3tggoBRztUE'

# Token
access_token = '738913391910195205-vDniBpj1YexCw4HMrboKrBf41ExGPbk'
access_token_secret = 'pu9CGUnRpTed3xz8fIT8gyhoZSWScZMybwhM8ScdNhJnj'

twitter = Twitter(consumer_key, consumer_secret, access_token, access_token_secret)
twitter.tweet('Testando minha biblioteca do Twitter')
