# Importando Bibliotecas Externas
import sys # Comunicação com o Sistema Operacional

# Retorna o local do arquivo
argumentos = sys.argv # Arg1 Metodo // Arg2 N1 // Arg3 N2

def soma(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

if argumentos[1] == "soma":
    resposta = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    resposta = sub(float(argumentos[2]), float(argumentos[3]))

print(resposta)



