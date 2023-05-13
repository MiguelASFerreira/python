import os
os.system("cls")
print("------------------------------")
produto = input("Nome do produto? ")
valor = float(input("Digite o valor do produto? "))
parcela = int(input("Digite o número de parcelas? "))

print("O {0} custa {1:.2f} e o número de parcelas é de {2}".format(produto,valor,parcela))
parcelas = valor / parcela
print("O valor das parcelas é de {0:.2f}".format(parcelas))
print("------------------------------")
