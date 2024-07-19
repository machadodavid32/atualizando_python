carrinho = []
produto = ''

while produto != 'sair':
    print("Por favor, informe os produtos a serem incluidos no carrinho:")
    produto = input()
    if produto != 'sair':
       carrinho.append(produto)
    else:
        print("Boa(s) escolha(s)")
        break   

print(f'Produtos no carrinho {carrinho}' )
print(f' Ultimo produto: {produto}')


    