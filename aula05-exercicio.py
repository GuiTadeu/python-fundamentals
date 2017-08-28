print('\nFESTA DO GUI')
print('---------------')

quantidade_convidados = range(int(input('Digite quantas pessoas irão participar da festa: ')))
lista_convidados = []

for convidado in quantidade_convidados:
    lista_convidados.insert(convidado, input('Digite seu Nome: '))

print('\nLISTA DE CONVIDADOS')
print('------------------------')

for convidado in quantidade_convidados:
    print(lista_convidados[convidado])

