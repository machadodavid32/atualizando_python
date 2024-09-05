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



