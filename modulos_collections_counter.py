# Modulo collections counter(contador) ou high performance container datetypes
# Tem chave e valor, sendo chave o elemento e valor a quantidade de ocorrências deste elemento


from collections import Counter

lista = [1, 1, 1, 2, 2, 2, 4, 4, 3, 3, 3, 5, 5, 5, 5, 5]
res = Counter(lista)
print(type(res)) # <class 'collections.Counter'>
print(res)

# Ele conta quantos elementos tem como resposta: Counter({5: 5, 1: 3, 2: 3, 3: 3, 4: 2})

print(Counter('david')) # Cria elementos e seus valores
# Counter({'d': 2, 'a': 1, 'v': 1, 'i': 1}) 

texto = '''I wake up in the morning and the first thing I do is brush my teeth.
After that, I´m going to breakfast and I go up stairs'''

# Separando por palavras
palavras = texto.split()
contagem_palavras = Counter(palavras)

# Obtendo as 5 palavras mais comuns
palavras_comuns = contagem_palavras.most_common(5)
print(palavras_comuns)