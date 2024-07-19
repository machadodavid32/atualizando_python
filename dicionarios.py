# Dicionários cont
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

