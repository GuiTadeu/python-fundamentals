nomes = ['Guilherme', 'Gabi', 'Gabriel']

# Laço FOR
# Para cada nome, dentro de nomes me mostra o nome
# Nome pode ser qualquer coisa, ele é um item
for nome in nomes:
    print(nome)

# Função RANGE() cria uma lista de numeros
# Tambem podemos determinar intervalos como por exemplo
# Range(5,10), vai contar do 5 ao 10
# Podemos usar o Passo tambem
# Range(0,100,2), vai contar de 0 a 100 com passo 2 (mostra os numeros pares)
lista_de_numeros = range(5)

for numero in lista_de_numeros:
    print(numero)

# Usando o Range no For
# 0,1,2,3
for item in range(3):
    print(nomes[item])

# Usando o Len para retornar o tamanho da lista
for i in range(len(nomes)):
    print(nomes[i])
    nomes.append('Adicionado')
    print(nomes)

# Contador
for cont in range(100):
    print(cont)

# Pegando letras de strings (Tambem são coleções)
palavra = 'Guilherme'
for letra in palavra:
    print(letra)

# Laço WHILE (enquanto)
i = 0
while i < 10:
    print('i ainda é menor que 10: ', i)
    i = i + 1

print('Acabou o While, o i é igual a:', i)

# Podemos usar and e or no while para ele retornar verdadeiro
# Podemos usar o +=

i = i + 1
# Ambos são iguais
i += 1

lista_frutas = ['Maçã', 'Pera', 'Uva', 'Abacaxi', 'Goiaba']

count = 0

# Se não existisse a Função Len
for fruta in lista_frutas:
    count += 1

print(count)
print(len(lista_frutas))

# Usando o BREAK
numero = 0
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1

print('Saiu do While')
