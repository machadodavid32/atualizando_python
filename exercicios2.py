'''1 - Crie um programa que le 6 números inteiros, armazeneos na lista e em seguida mostre na tela os valores


lista: list[int] = []
while len(lista) < 6:
    valor: int = int(input(f'Informe o valor {len(lista) + 1}/6: '))
    lista.append(valor)
    
    
print(lista)

'''

''' 2 - Faça um programa que possua uma lista denominada A que armazene 6 números inteiros.
O programa deve executar os seguintes passos: 
1 - valores da lista: 1, 0, 5, -2, -5, 7 
2 - Armazene em uma variável inteira a soma entre os valores das posições A[0], A[1] e A[5] e mostre na tela a soma
3 - Modifique a lista na posição 5, atribuindo a esta posição o valor 100
4 - Mostre na tela cada valor da lista A, um em cada linha

A = [1, 0, 5, -2, -5, 7]
soma: int = A[0], A[1], A[5]
print(f'A soma dos valore solicitados é {sum(soma)}')
A[5] = 100

for valores in A:
    print(f'Valor em cada linha: {valores}')

'''

'''
3 - Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele possui.
''' 

valores: list[int] = []
contador_pares: int = 0
while len(valores) < 10:
    valor = int(input(f"Por favor, informe o valor {len(valores) + 1}/10: "))
    valores.append(valor)
    
    if valor % 2 == 0:
        contador_pares = contador_pares + 1

if contador_pares> 0:
    print(f'Valores{valores} possui {contador_pares} pares')
else:
    print('A lista não possui valores pares')
        
            
        
    
    
      
    
    
    
    
    