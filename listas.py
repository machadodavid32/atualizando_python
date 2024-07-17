"""

lista1 = [1, 1, 3 ,4 ,5, 10, 100, 3, 56.7]

print(lista1)

if 'd' in lista1:
    print("achei")
else:
    print('não achei')    

print(lista1.sort()) # Comando sort() ordenar uma lista    
print(lista1)

print(lista1.count(3)) # comando count() lista quantos números 3 tem na lista

lista1.append(123)
print(lista1)
"""


"""
lista1 = [1, 1, 3 ,4 ,5, 10, 100, 3, 56.7]
lista2 = ([5, 6, 8])
if [5, 6, 8] in lista2:
    print("Achei")


lista2.extend([12, 44, 57, "Aline", "Arthur"])
print(lista2)
    
# Com append vc pode adicionar apenas um elemento. Com extend vc pode adicionar mais de um elemento
# usando [] exemplo. lista2 = [12, 44, 55] vai adicionar estes 3 em vez de um.

lista2.insert(3, "machado") # insert tem dois arugmentos, vc escolhe em qual indice via adicionar novo elemento
print(lista2)    

lista3 = lista1 + lista2 # vai criar uma nova lista com a soma das lista
print("lista 3 é #######", lista3)

lista3.reverse()
print("Lista 3 reversa é ###### ",lista3)

print(lista1[::-1]) #outro modo de inverter as lista
print(lista2[::-1])

lista6 = lista2.copy() # copia todos os dados de uma lista em uma nova lista
print(lista6)

print(len(lista6)) # Conta quantos elementos tem na lista

lista6.pop() # sem colocar argumento, ele elimina o ultimo.
print("Eliminando ultimo item lista 6", lista6)

lista1.pop(1) # elimina elemento no indice1
print(lista1)

lista7 = ["Romario", "Bebeto", "Zinho", "Mazinho"]
lista7.clear() # Vai zerar a lista
print(lista7)

lista = []
tuplas = ()

lista8 = [1, 3, 5, 15]
lista8 = lista8 * 3  # multiplica a lista
print(lista8)


# Converter uma STRING em uma lista[]
lista9 = "David de Araújo Machado"
print(lista9.split()) # split automaticamente transforma um texto em lista separando por espaços.
# resposta: ['David', 'de', 'Araújo', 'Machado']

# Transformando uma lista em uma STRING
lista10 = "".join(lista9) # aqui coloquei espaço, mas pode colocar qualquer caracter
print(lista10)

lista10 = "#".join(lista10) # Exemplo adicionando outro caracter
print(lista10)

for elemento in lista10:
    print(f'Lista 10 é {elemento}')
"""    


"""
lista11 = [56, 58, 18, 87]
soma = 0
for elemento in lista11:
    print(elemento)
    soma = soma + elemento
print(f'A Soma é {soma}')

carrinho = []
produto = ''

while produto != "sair":
    print("Adicione um produto na lista ou digite sair: ")
    produto = input()
    if produto != "sair":
        carrinho.append(produto)
        
print("Total de produtos")
for produto in carrinho:
    print(produto)
     
print(f'total de produtos ',produto)
print(carrinho)    
"""

cores = ["preto", "branco", "vermelho"]

print(cores[2]) # busca por indice
print(cores[-3]) # busca por indice de forma inversa

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)


numeros = [1, 5, 6, 7, 8, 9, "Playstation", 10, 15]
# procurando o indice de um elemento na lista
print(numeros.index(6)) # o elemento 6 está no index 2
print(numeros.index("Playstation")) # Procurando o index do elemento playstaion = 6

print(numeros.index(10, 3)) # Buscando elemento 10 a partir do index 3
print(numeros.index("Playstation", 2))

#slice - inicio, fim, passo
print(numeros[2:]) # pegando elementos a partir do index dois
print(numeros[2:8]) # pegando elementos do index dois até index 8
print(numeros[::2]) # pegando elementos do index em dois em dois

# trocando elementos. Elemento na posição zero vai trocar de lugar com o da posição 6
numeros[0], numeros[6] = numeros[6], numeros[0]
print(numeros)
    
# matematica em listas
numeros2 = [1, 2, 50, 500, 800,  900, 521.5]
print(sum(numeros2)) # soma
print(max(numeros2)) # Encontra o maior elemento da lista
print(min(numeros2)) # Encontra o menor elemento da lista
print(len(numeros2)) # Quantos elementos tem na lista

# Tipo de dados usando type
print(type(numeros2)) # resposta> list

# Transformando uma lista [] numa tupla ()
tupla = tuple(numeros2)
print(numeros2)
print(type(tupla))


# deep copy - copia uma lista sem alterar a antiga
listanova = numeros.copy()
print(listanova)
listanova.append("Switch") # a antiga lista não será alterada.
print(numeros)
print(listanova)
          
# Shallow copy - copia uma lista, se alterar essa nova lista, a antiga também será alterada.

nova = listanova
print(listanova) # ['Playstation', 5, 6, 7, 8, 9, 1, 10, 15, 'Switch']
nova.append("Nintendo")
print(listanova) # ['Playstation', 5, 6, 7, 8, 9, 1, 10, 15, 'Switch', 'Nintendo']
print(nova) # ['Playstation', 5, 6, 7, 8, 9, 1, 10, 15, 'Switch', 'Nintendo']


          