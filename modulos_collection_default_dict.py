"""
Parecido com um dicionário, o default_dict pode evitar erros quando, por exemplo, acessar uma chave que não existe.
Podemos criar um valor padrão para chaves que não existem.    
"""

from collections import defaultdict

# Vamos usar as funções lambda, cujo podem ou não receber valores de entrada e retornar valores.

dicionario = defaultdict(lambda: 0) # Neste caso, estamos fazendo um dicionario que não recebe entrada e retorna valor zero
# print(dicionario)
# defaultdict(<function <lambda> at 0x00000251151204A0>, {}) Reparar o colchetes no final, está vazio mas não gerou erros.

dicionario['curso'] = 'programação em python'
print(dicionario)
# efaultdict(<function <lambda> at 0x000001BE1D7E04A0>, {'curso': 'programação em python'}) # veja que ele adicionou uma chave e valor

print(dicionario['outro']) # reparar que esta chave não existe
# Resposta: 0 -> evitando erros

print(dicionario)
