import os
os.system("cls")
print("------------------------------")
nome = input("Digite seu nome? ")
salario = float(input("Digite o Salário? "))
aumento = float(input("Digite a porecentagem de aumento? "))

aumento = salario * aumento / 100
print("O aumento é: ",aumento,)
salario = salario + aumento
print("Salário total: ", salario)
print("-------------------------------")
print("Olá, {0}, seu aumento é de {1:.2f}, e seu novo salário é de {2:.2f}".format(nome, aumento, salario))