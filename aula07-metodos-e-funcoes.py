# Métodos e Funções
# Função retorna
# Método não
# Não precisa de especificar o tipo do parametro
def soma(n1,n2):
    resultado = n1 + n2
    return resultado

retorno = soma(75,1288)
print(retorno)

# Método sem retorno
def imprime_oi():
    print('OI')

imprime_oi()


# Contando itens no IF com função
def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

if tem_sete_itens('1234567'):
    print('Tem sete itens')
else:
    print('Não tem sete itens')



