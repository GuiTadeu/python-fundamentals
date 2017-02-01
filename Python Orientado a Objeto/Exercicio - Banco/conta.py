# Cada Conta possui: Cliente(Dono), Saldo, Limite negativo,
# Métodos: Sacar, Depositar, Consultar Saldo

from cliente import Cliente

class Conta:

    def __init__(self, cliente, saldo, limite):

        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def sacar(self,quantidade):
            self.saldo -= quantidade

    def depositar(self, quantidade):
            self.saldo += quantidade
