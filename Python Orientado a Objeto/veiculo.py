# Definimos um objeto através de classes
# A classe é a receita do objeto, é a planta da casa
# O objeto é quando pegamos a classe e instaciamos ela, criamos um objeto real a partir da classe

# Letra Maiuscula para classe
# O Self é semelhante ao This do Java, ele passa ele mesmo para dentro do método
# O objeto passa ele mesmo para dentro do método
# Método __init__ é um método construtor, ele constrói o objeto
# Quando instanciar o primeiro método a ser rodado é o __init__ com seus devidos parametros
# Parametro Self
class Veiculo:

    def __init__(self, cor, rodas, marca, tanque):

        # Recebe do Parametro
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros