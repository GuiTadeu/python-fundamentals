def maior_numero(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

def menor_numero(lista):
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor

lista_numeros = [-5, 70, 2, 14, 1, 0, -154, 40, 5, 3, 800, 60, 7, 8, -3]
maior = maior_numero(lista_numeros)
menor = menor_numero(lista_numeros)
print('O maior numero da lista é o', maior, 'e o menor é o', menor)
