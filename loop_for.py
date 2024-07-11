nome = "david"
for letra in nome:
    print(letra)

lista = [1, 2, 5, "david", "machado", "aline", "Arthur", True] 
for letra in lista:
    print(letra)

for numero in range(5, 15):
    print(numero)
    
for indice, letra in enumerate(nome):
    print(nome[indice])           
    
for valor in enumerate(nome): # enumerate serve para informar o indice de cada caracter
    print(valor)
# resposta: 
# (0, 'd')
# (1, 'a')
# (2, 'v')
# (3, 'i')
# (4, 'd')    