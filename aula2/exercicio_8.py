valor = float(input("Valor do produto? \n"))

if (valor >= 100):
    valor -= valor * 10/100
    print(f"O valor final com desconto de 10% é {valor:.2f}")
elif (valor >= 50):
    valor -= valor * 5/100
    print(f"O valor final com desconto de 5% é {valor:.2f}")
else:
    print(f"O valor final sem desconto é {valor:.2f}")