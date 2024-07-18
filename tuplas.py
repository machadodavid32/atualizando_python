"""

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


tupla4 = (1, 5, 6, 8, 700, 100)
print(sum(tupla4))
print(max(tupla4))
print(min(tupla4))
print(len(tupla4))

print(5 in tupla4) # número está na tupla4? resposta: True


# iterando em uma tupla

for n in tupla4:
    print(n)

for indice, n in enumerate(tupla4):
    print(indice, n)

tupla5 = ('a', 'b', 'c', 's', 'g', 'a', 'a')
print(tupla5.count('a')) # quantos 'a' eu tenho Resposta 3
print(tupla5.count('b')) # quantos 'b' eu tenho Resposta 1

"""


# Transformando uma string em tupla

carro = tuple("Hyundai ix 35")
print(carro)

# Acessando via indice

print(carro[2]) # resposta u

print(carro[1:5]) 

print(carro[::-1])

# Achando um index
print(carro.index("x")) # resposta index 9







    
    
        


