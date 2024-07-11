print("Informe a idade do capanga ")

idade = input()
idade = int(idade)

if idade <= 17:
    print("Menor de idade")
elif idade >= 18 and idade <= 39:
    print("Maior de idade")
elif idade >= 40 and idade <=60:
    print("Meia idade")         
else:
    print('velhote')
        