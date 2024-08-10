from collections import namedtuple
# São tuplas nomeadas, portanto, precisamos definir nome e parâmetro.

# Declaração namedtuple forma 1

cachorro = namedtuple('cachorro', 'idade raca nome')

# Declaração namedtuple forma 2
cachorro = namedtuple('chacorro', 'idade, raca, nome')

# Declaração namedtuple forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# usando
ray = cachorro(idade=2, raca='vira lata', nome='Ilton')
print(ray)

print(ray[0]) # Acionando elementos
print(ray.idade) # acionando elementos de outra forma

# Qual é o indice
print(ray.index('Ilton')) # indice 2

# Quantas ocorrências deste valor tem na tupla
print(ray.count('vira lata')) # 1 ocorrência

