'''
def nome_da_funcao(parametros de entrada):
    bloco_da_funcao
    '''
# Criando uma função    
def diz_algo():
    fale = input("Diga algo: ") 
    print(fale)

# Executando uma função
diz_algo()       

# Podemos atribuir uma função a uma variavel.
fale = diz_algo
fale()


# Função com retorno
def soma(a, b):
    return a + b

# Usando a função criada com retorno
valor_total = soma(10, 30)
print(valor_total)