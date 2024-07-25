# Dicionários cont

"""
dicionario = {'david':'Machado', 'Aline': 'Machado', 'Arthur': 'Machado'}
paises = {'br': 'Brasil', 'us': 'USA', 'ar': 'Argentina', 'es': 'Espanha'}

# Acessando index - o acesso ai index é feito pela chave
print(dicionario['david'])
print(paises['es'])

# Forma mais comum e correta de acessar o index do dicionario é o get, pois caso não exista
# a chave, ele não da erro e retorna none

print(paises.get('us'))  # resposta USA
print(paises.get('ru')) # resposta None

# outra forma de usar o get
# Criar uma variável para informar que a chave não existe
pais = paises.get('pa', 'País não encontrado')
print(pais)
# Resposta: Em vez de retornar None, ele retorna: País não encontrado

# Achando uma chave no dicionario usando in - vai retornar True ou False
print('br' in dicionario) # False
print('br' in paises) # True
print('us' in pais) # False
# Acima, o in sempre busca pela CHAVE


#Dicionarios podem receber qualquer tipo de dado. Inclusive tuplas
telefones = {
    (555-5555): 'sp',
    (54545-5555): 'rj',
    (54577-878): 'rs'
    }

print(telefones)


# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 100, 'mar': {500}, 'Abr': {400}}
receita['mai'] = 800
print(receita) # {'jan': 100, 'fev': 100, 'mar': {500}, 'Abr': {400}, 'mai': 800}

# Atualizando um dicionário
receita.update({'mar': 600}) 
print(receita)

# Remover dados de um dicionário
receita.pop('jan') # no caso do dicionário, o pop usa a chave para remover iténs
print(receita)

# Outra forma de remover iténs
del receita['fev']
print(receita)

receita.update({'jan': 300})
receita.update({'fev': 500})
print(receita)

carrinho = []
produto1 = {'nome': 'ps5', 'quantidade': 30, 'preço': 4100}
produto2 = {'nome': 'ns', 'quantidade': 50, 'preço': 1900}
carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
carrinho.append({'nome': 'xbox', 'quantidade': 20 ,'preço': 2900})
print(carrinho)
"""

dicionario2 = dict(a=2, c=3, b=5, t=80)
print(type(dicionario2))

# limpar dicionário
dicionario2.clear()
print(dicionario2)

dicionario3 = dict(a=2, c=3, b=5, t=80, y=40)

# Copiando um dicionário modo 1 (deep copy - sem alterar a original)
copiando = dicionario3.copy()
copiando ['df'] = 54 # atualizando colocando uma chave a mais
print(copiando)
print(dicionario3)


# Copiando um dicionário modo 2 (shallon copy - original também é alterado)
copiando = dicionario3
copiando['sp'] = 120
print(copiando)
print(dicionario3)

receita = {'jan': 100, 'fev': 100, 'mar': 500, 'Abr': 400}

for chave in receita:
    print(chave)
    

# melhorando    
for chave in receita:
    print(f'{chave}: {receita[chave]}')
    
    
# Acessando somente as chaves
print(receita.keys())  # dict_keys(['jan', 'fev', 'mar', 'Abr'])

for chave in receita.keys():
    print(receita[chave])

# Acessando somente os valores
print(receita.values())  # dict_values([100, 100, 500, 400])

for valor in receita.keys():
    print(receita[valor])
    
# Descompactando com items()
for chave, valor in receita.items():
    print(f'chave: {chave} e valor: {valor}')    
    
    

# Também da pra somar, ver qual é o maior valor, menor, 
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))

