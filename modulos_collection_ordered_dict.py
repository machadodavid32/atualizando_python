
"""Ordered dict é um dicionário que garante que os valores serão colocados na ordem certa"""
from collections import OrderedDict

dicionario = {'a': 10, 'b': 12, 'd':14, 'f': 19}
print(dicionario)
# lembrar que dicionários não garantem a impressão dos valores na ordem. As vezes acontece, as vezes não acontece.

dicionario = OrderedDict({'a': 10, 'b': 12, 'd':14, 'f': 19})

for chave, valor in dicionario.items():
    print(f'chave = {chave} e valor{valor}')
    
# Resposta: 
# {'a': 10, 'b': 12, 'd': 14, 'f': 19}
# chave = a e valor10
# chave = b e valor12
# chave = d e valor14
# chave = f e valor19    

dicionario2 = {'a': 1, 'b': 2}
dicionario3 = {'b': 2, 'a': 1}

print(dicionario2 == dicionario3) # Dicionário 2 é igual ao dicionário 3?
# True - as ordens do elemento não importa pro dicionário

dicionario4 = OrderedDict({'a': 1, 'b': 2})
dicionario5 = OrderedDict({'b': 2, 'a': 1})
print(dicionario4 == dicionario5)
# False pois no orderedDict a ordem importa

