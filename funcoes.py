'''
def nome_da_funcao(parametros de entrada):
    bloco_da_funcao
 
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

def div(c, d):
    return c/d

divisao = div(50, 2)
print(divisao)


from random import random

def joga_moeda():
    valor = random()
    if valor >= 0.5:
        return 'Cara'
    return 'Coroa'
    

print(joga_moeda())
     '''

# Função com parâmetro
def quadrado(numero):
    return numero * numero

print(quadrado(3)) 

# A ordem dos parâmetros importa
def nomes(nome, sobrenome):
    return f"Seu nome completo é {nome} {sobrenome}"

print(nomes("David", "Machado"))


# Parâmetro nomeado
print(nomes(nome='Aline', sobrenome='Guedes')) # nomeado


def soma_impares(numeros):
    total = 0 # dando um valor pra variável
    for num in numeros:
        if num % 2 != 0: # se o número for impar
            total = total + num # total = total + cada num impar
    return total # return fica fora do if pra dar corretamente o resultado de soma

lista = [11, 2, 6, 8, 17, 35]
print(soma_impares(lista)) # resultado: 63 - somou somente os impares da lista


         
# Funções com parâmetro padrão  
def exponencial(numero, potencia=2): # dando um valor ao parâmetro, ele se torna opcional ao usar a função
    return numero ** potencia

# OBS: Os parâmetros padrão devem estar no final da declaração(numero, potencia=2)

print(exponencial(3)) # Sem informar o segundo parâmetro - padrão é 2
print(exponencial(2, 3)) # Aqui informo o padrão - vai substituir o 2 
          