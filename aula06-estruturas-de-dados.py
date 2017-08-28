# Lista (LIST)
# Pode ser vazia
# Infinita
# Mutavel
# Um item de cada vez
minha_lista = ['Gui', 'Gabi', 'Gabriel']

# Tupla (TUPLE)
# Não é mutavel
# Posso mudar o valor dos objetos mas nao posso remover
# É como uma constante, sempre o mesmo tamanho
# Só aceita quando subistituir ela toda
minha_tupla = ('Gui', 'Gabi', 'Gabriel')

# Dicionario (DICT)
# O valor pode ser qualquer valor
# Hash Map, Hash Table
meu_dicionario = {'nome': 'Guilherme', 'idade': 17}

# Conjunto (SET)
# Não podem ter dois itens repetidos
# Mutavel
# Não tem indice, não é ordenado
meu_conjunto = {'Gui', 'Joao'}

# Perguntando se algo está na list, tupla, set. Só não acha no dicionario
if 'Gui' in minha_tupla:
    print('Gui está na tupla')

# Perguntando se algo está no dicionario
if 'Guilherme' in meu_dicionario.values():
    print('Guilherme está no Dicionario')

# Pesquisa no Dicionario (Melhor que lista na busca)
# Retorna o nome Guilherme
# Se usar com letra minuscula tem q por minuscula
print(meu_dicionario['nome'])

# Qualquer coleção da para contar itens com o len
print(len(meu_conjunto))

# Pega os valores, vem desordenado
for valores in meu_dicionario.values():
    print(valores)

# Pegando chaves
for chaves in meu_dicionario.keys():
    print(chaves)

# Mudando valores das chaves
meu_dicionario['nome'] = 'Gabi'
print(meu_dicionario)

# Adicionando novos itens
meu_dicionario['endereco'] = 'Rua dos Bobos'
meu_dicionario['telefone'] = '70707070'
print(meu_dicionario)

# Adicionando itens no conjunto
meu_conjunto.add('Gabriel')

# Isso não vai acontecer pois não pode haver itens repetidos
meu_conjunto.add('Gui')

# Procurando no conjunto
# É mais rapido
# Na lista ele percorre a lista inteira, um bilhão de comparações
# O primeiro é? Não, o segundo? Não
# A lista é ordenada. O Conjunto não
# O Conjunto é uma tabela Hash
# Cada palavra é transformada num código
# O código é transformado numa tabela
# A busca é instantanea
# O Dicionario tambem é assim
if 'Gui' in meu_conjunto:
    print('Foi encontrado dentro do Conjunto')

# Removendo itens do conjunto
meu_conjunto.remove('Gabriel')

# Como iniciar vazio
lista = []
tupla = ()
dicionario = {}
conjunto = set()

# Aninhamento de dados
loucura = [(1,2), (3,4), (5,6), ({'joao', 'maria'}, {'gabriel'})]
print(loucura)





