'''1 - Crie um programa que le 6 números inteiros, armazeneos na lista e em seguida mostre na tela os valores'''


lista: list[int] = []
while len(lista) < 6:
    valor: int = int(input(f'Informe o valor {len(lista) + 1}/6: '))
    lista.append(valor)
    
    
print(lista)

    
    
    
    
    
    