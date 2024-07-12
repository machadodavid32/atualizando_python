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

qtd = int(input("Quantas vezes este loop pode se repetir? "))
for n in range(1, qtd+1):
    print(f'quantos mesmo  {n}')
    

    
repetir = int(input('Quantas vezes esse deve repetir?'))
for n in range(1, repetir + 1):
    print(f'Deve repetir {n} vezes')


qtd = int(input("Este aqui, vamos somar, quantas vezes deve rodar?"))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f"Informe o número{n}/{qtd} valor"))
    soma = soma + num
    print(f"a soma é {soma}")
    
    