# As tuplas são imutáveis

tupla = (1, 2, 3, 4) # Exemplo de tupla

tupla1 = 1, 2, 3, 4, 5 # outro forma de tupla

print(type(tupla)) # <class 'tuple'>
print(type(tupla1)) # <class 'tuple'>

# Criando uma tupla com range
tupla2 = tuple(range(1, 11))
print(tupla2) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

tupla3 = tuple(range(5, 20, 2))
print(tupla3) # (5, 7, 9, 11, 13, 15, 17, 19)


# Descompactando uma tupla. obs: para cada elemento, uma variável será criada.
frase = ("Internation", "SuperStar")
separar, descompactar = frase
print(separar) # Internation
print(descompactar) # SuperStar




