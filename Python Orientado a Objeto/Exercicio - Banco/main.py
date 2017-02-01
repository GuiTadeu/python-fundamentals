'''
Crie um Software de Gerenciamento Bancario
Esse software podera ser capaz de criar Clientes e Contas
Cada Cliente possui: Nome, CPF, Idade
Cada Conta possui: Cliente(Dono), Saldo, Limite negativo,
métodos: Sacar, Depositar, Consultar Saldo
'''
from cliente import Cliente
from conta import Conta

print('BANCO DO TIO GUI')
print('---------------------')

cliente_1 = Cliente('Guilherme', 393595875, 17)
conta_cliente_1 = Conta(cliente_1, 1000, 500)
print('\n1 - Consultar dados Cliente \n2 - Consultar Saldo \n3 - Sacar \n4 - Depositar')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    print('Nome:', conta_cliente_1.cliente.nome)
    print('CPF:', conta_cliente_1.cliente.cpf)
    print('Idade:', conta_cliente_1.cliente.idade)
elif opcao == 2:
    print('Seu saldo é de: R$', conta_cliente_1.saldo)
elif opcao == 3:
    conta_cliente_1.sacar(200)
    print('Você sacou e agora seu saldo é de: R$', conta_cliente_1.saldo)
elif opcao == 4:
    conta_cliente_1.depositar(500)
    print('Você depositou e agora seu saldo é de: R$', conta_cliente_1.saldo)
else:
    print('Numero Invalido')