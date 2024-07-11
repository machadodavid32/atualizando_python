print("Informe o nome do funcionário")
nome = input()

print("Informe o RA do funcionário")
ra = int(input())

print("Informe o salario do funcionário")
salario = float(input())

print("Agora calculando aumento")
percentual = 15
percentual /= 100
aumento = salario * percentual
novo_salario = salario + aumento
print("Salario que era de", salario, "agora é de", novo_salario)
