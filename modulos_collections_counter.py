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
print(Counter(texto)) # Separando por caracteres
# Counter({' ': 15, 't': 6, 'e': 5, 'i': 5, 'n': 5, 'h': 5, 'r': 3, 's': 3, 'I': 2, 'a': 2, 'u'
# : 2, 'm': 2, 'o': 2, 'g': 2, 'd': 2, 'w': 1, 'k': 1, 'p': 1, 'f': 1, 'b': 1, 'y': 1})

palavra = texto.split() # Separando por palavras
print(Counter(palavra))
# Counter({'I': 2, 'the': 2, 'wake': 1, 'up': 1, 'in': 1, 'morning': 1, 'and': 1, 'first': 1,
# 'thing': 1, 'do': 1, 'is': 1, 'brush': 1, 'my': 1, 'teeth': 1})

