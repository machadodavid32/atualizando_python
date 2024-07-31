# Conjuntos também utilizam as chaves {}, porem, só tem valores
# Conjuntos são MUTAVEIS
# Ao imprimir, não será na ordem e NÃO TEM VALORES REPETIDOS, mesmo se vc coloque ele não imprime
conjunto = {5, 7, 9, 10}
print(conjunto)
print(type(conjunto))


if 9 in conjunto:
    print("tem")
else:
    print("não tem")    

lista = [10, 10, 12, 5, 7, 54,]
print(f'{lista} e temos {len(lista)} elementos')

tupla = (10, 10, 12, 5, 7, 54,)
print(f'{tupla} e são {len(tupla)} elementos')    

dicionários = {}.fromkeys([10, 10, 12, 5, 7, 54,], 'valor') # Aqui estamos adicionando valor as chaves
print(f'{dicionários} e são {len(dicionários)} elementos')

conjuntos = {10, 10, 12, 5, 7, 54,}
print(f'{conjuntos} e são {len(conjuntos)} elementos')

# Acima, os dicionários não repetem chave, portanto, mostra somente 5 elementos
# Os conjuntos não repetem valores, portanto, mostra somente 5 elementos
# Já as tuplas e listas, repetem valores, portanto, mostram todos os 6 elementos

# Sets aceitam qualquer tipo de valor
conjunto2 = {'david', True, 5, False}

for valor in conjunto2:
    print(valor)


# Como os sets não repetem valores, eles podem ser eficientes para filtrar os dados   
lista = [10, 10, 12, 5, 7, 54, 10, 5, 80, 80,]
print(set(lista))
# Dados acima foram filtrados> {5, 7, 10, 12, 80, 54}


# Adicionando elementos em um conjunto
conjunto.add("Adicionando")
print(conjunto)

# Removendo elementos forma 1 utilizando remove
conjunto.remove("Adicionando") # obs: Caso não encontre o valor, dará erro.
print(conjunto)

# Removendo elementos forma 2 utilizando o discard
conjunto.discard(7) # caso o valor não seja encontrado, não dará erro.
print(conjunto)


# Copiando um conjunto, forma 1, deep copy (sem alterar original)
novo = conjunto2.copy()
novo.add("correr") # Adicionando um elemento a mais
print(conjunto2)
print(novo)

# Copiando um conjunto, forma 2, shallow copy - original também será alterado
novo2 = novo
novo2.add("Skuls")
print(novo2)
print(novo)

# Revomento todos os iténs de um conjunto
novo2.clear()
print(novo2)


# Unindo dois conjuntos
# Precisamos gerar um conjunto com nomes de estudantes unicos
# Forma 1
python = {"David", "Julia", "Almeida", "Chico", "Tavares", "Sonia"}
java = {"David", "Julia", "Costa", "Araújo", "Souza", "Sonia"}
juntos = python.union(java)
print(f'Estudando Python e javas juntos: {juntos}')

#Forma 2
unicos2 = python | java
print(unicos2)


# Gerando um conjunto com os estudantes que estão cursando os dois cursos
# Forma 1
ambos = python.intersection(java)
print(ambos)
# Resposta: {'Julia', 'David', 'Sonia'}

# Forma 2
ambos1 = python & java
print(ambos1)


# Gerando um conjunto de estudantes que estudam em um curso apenas
so_python = python.difference(java)
print(f'Só estudando python temos: {so_python}')
# Só estudando python temos: {'Tavares', 'Almeida', 'Chico'}

so_java = java.difference(python)
print(f'Só estudando java temos: {so_java}')
# Só estudando java temos: {'Costa', 'Souza', 'Araújo'}

# Da pra fazer coisas matematicas com sum, max, min, len desde que os valores sejam reais ou inteiros