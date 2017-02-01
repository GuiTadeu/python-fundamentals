# Onde meu programa vai rodar
# Caracteristicas, Funções
# Importando o Veiculo
# De dentro do arquivo veiculo importa a classe Veiculo
from veiculo import Veiculo
from carro import Carro

# Temos que passar os três argumentos obrigatórios
caminhao_rosa = Veiculo('Rosa', 6, 'Ford', 10)

print(caminhao_rosa)

# Criamos um tipo no Python :D
print(type(caminhao_rosa))

print('\nDESCREVENDO OBJETO')
print('-----------------------------')

print('\nCAMINHÃO ROSA:')
print('Cor:', caminhao_rosa.cor)
print('Rodas:', caminhao_rosa.rodas)
print('Marca:', caminhao_rosa.marca)
print('Tanque:', caminhao_rosa.tanque)

print('\nCARRO AZUL:')
carro_azul = Carro('Azul', 'BMW', 30 )
print('Cor:', carro_azul.cor)
# Não preciso passar: print('Rodas:', carro_azul.rodas)
print('Marca: ', carro_azul.marca)
print('Tanque:', carro_azul.tanque)

# Usando o Método Abastecer
print('\nABASTECIDO:')
carro_azul.abastecer(35)
print('Tanque:', carro_azul.tanque)



