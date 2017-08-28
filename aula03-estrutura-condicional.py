print('EXÉRCITO ALISTAMENTO')
print('-----------------------')

idade = float(input('Digite sua Idade: '))
peso = float(input('Digite seu Peso: '))
altura = float(input('Digite sua Altura: '))

if ((idade > 18 and peso >= 60) and altura >= 1.70):
    print('Você pode se alistar')
else:
    print('Você não pode se alistar')


