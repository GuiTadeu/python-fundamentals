# Precisamos usar o \\ no Windows pq se usarmos uma pode ser considerado um caracter especial
# Por exemplo o \n
# No Linux não precisa pois as barras são para direita /

# O Método Open leva dois argumentos, nome do arquivo, modo de abertura
# Não escrever nada abre o modo R
# R - Read
# W - Write, se não existir ele cria um
# Se ja tiver algo nele ele vai apagar e criar um novo
# R+ - Lê e escreve (Primeiro Lê, por isso tem que existir)
# A - Append, adiciona, não apaga, tudo q eu mudar ele vai jogando lá e tals, de 1 a 1000, com append add mais um 1 mil
# B - Bytes, se não for texto abre com o B (imagens e etc)


arquivo = open('arquivo.txt', 'r')

'''
Como escrever no Arquivo?
arquivo = open('arquivo.txt', 'w')
for i in range(1, 1001):
    arquivo.write('AAA'+str(i)+'\n')

'''

'''
Lendo arquivo
arquivo_read = open('arquivo.txt', 'r')
Método Read
print(arquivo_read.read())

'''

# Como passar de linha em linha?
for linha in arquivo:
    print(linha)

# RB - Read Binary
arquivo_imagem = open('logo.png', 'rb')
print(arquivo_imagem.read())