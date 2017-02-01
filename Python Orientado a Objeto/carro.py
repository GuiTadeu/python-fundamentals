# Herança em POO
from veiculo import Veiculo
class Carro(Veiculo):
    # Chamando o Carro
    def __init__(self, cor, marca, tanque):
        # Chamando o Veiculo
        # Criando um Carro sempre com 4 rodas
        Veiculo.__init__(self, cor, 4, marca, tanque)

    # Sobreposição de Métodos
    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print('Erro: Tanque cheio')
        else:
            self.tanque += litros