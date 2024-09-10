dicionario = {'a':1, 'b':2, 'c':3, 'd':4}
quadrado = {chave: valor **2 for chave, valor in dicionario.items()}
# Acima ele vai levar os valores ao quadrado e usar items() para retornar as chaves e valores
print(quadrado)
# {'a': 1, 'b': 4, 'c': 9, 'd': 16}

# Criando um dicionário com compreensão
tupla = (1, 2, 3, 4)
quadrado = {valor: valor ** 2 for valor in tupla}
print(quadrado) 
# Resposta: {1: 1, 2: 4, 3: 9, 4: 16} Criou-se um dicionário com chave e valor

res = {quad: ('par' if quad % 2 == 0 else 'impar')for quad in quadrado}
print(res)
# Resposta: {1: 'impar', 2: 'par', 3: 'impar', 4: 'par'}

