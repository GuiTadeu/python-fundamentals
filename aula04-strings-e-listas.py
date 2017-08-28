frase = 'Oi, tudo bem?'
lista_nomes = ['Guilherme', 'Gabi', 'Gabriel']

# Imprimindo o Item 1
print(lista_nomes[1])

# Cortando da letra 0 até a letra 5
print(frase[0:5])

# Cortando da letra 0 até a letra 10 com passo 2
print(frase[0:10:2])

# Para contar de trás para frente
# Gabriel [-1], Gabi [-2], Guilherme [-3]
print(lista_nomes[-3])

# Iria imprimir tudo, com o passo -1, assim imprimi ao contrario
print(frase[::-1])

# Operações

# Adicionar na lista
lista_nomes.append('Geraldo')

# Remover
lista_nomes.remove('Geraldo')

# Limpar toda lista
lista_nomes.clear()

# O Local onde eu quero insertir tal item
# Inserindo no elemento 1
lista_nomes.insert(1, 'Creosvaldo')

# Outro modo de fazer o método acima é o seguinte
lista_nomes[0] = 'Robervania'

# Contar quantos Joãos tem na lista
# Ou seja conta quantas vezes o item se repete
contador_joao = lista_nomes.count('João')

# Tamanho
print(len(frase))
print(len(lista_nomes)) # Retorna 5

# Pegar o ultimo item e remove-lo
print(lista_nomes.pop())

# Métodos de Strings

# Tudo em Minusculo
print(frase.lower())

# Tudo em Maiusculo
print(frase.upper())

# Separa a frase onde estiver tal caracter
# Transforma frase em lista
# Usamos a virgula para separar
frase_separada = frase.split(',')
print(frase_separada)
print(frase_separada[0])
print(frase_separada[1])

# Concatenando frases
frase_nova = frase + ' Como vai você?'
print(frase_nova)

