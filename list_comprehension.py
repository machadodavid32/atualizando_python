numeros = [10, 2, 5, 80, 74]
res = [numero * 10 for numero in numeros] # list comprehension
print(res)

res = [numero / 2 for numero in numeros]
print(res)


# utlizando list comprehension em funções
def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)

nome = "David Machado"
print([letras.upper() for letras in nome])
# resposta: ['D', 'A', 'V', 'I', 'D', ' ', 'M', 'A', 'C', 'H', 'A', 'D', 'O']

print([numero * 3 for numero in range(2, 90)])


number = [2, 5, 7, 8 ,40 ,122, 125]
pares = [numero for numero in number if numero % 2 == 0] # escolher os numeros pares
impares = [numero for numero in number if numero % 2 != 0] # Escolher par

print(pares) # [2, 8, 40, 122]
print(impares) # [5, 7, 125]

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in number]
print(res) # Resposta: [4, 2.5, 3.5, 16, 80, 244, 62.5] dobrou pares e dividiu impares



"""Listas aninhadas """
lista_aninhanda = [[1,2,3], [4,5,6], [7,8,9]]
print(lista_aninhanda[0][2]) # vai acessar o indice 2 dentro do indice 0

[[print(la) for la in lis] for lis in lista_aninhanda]
# vai imprimir todos os valores da lista, um em cada linha