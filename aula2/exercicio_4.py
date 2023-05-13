litros = float(input("Digite quantos litros você quer? \n"))
combustivel = input("Qual combustível você quer| Digite A para alcool e G para Gasolina| ? \n").upper()
preco = 0

if (combustivel == "A"):
    preco = litros * 1.9
    if (litros <= 20):
        preco -= 1.9 * litros * 3/100
    else:
        preco -= 1.9 * litros * 5/100
elif (combustivel == "G"):
    preco = litros * 2.5
    if (litros <= 20):
        preco -= 2.5 * litros * 4/100
    else:
        preco -= 2.5 * litros * 6/100

print(f"O seu combustível é {'Alcool' if combustivel == 'A' else 'Gasolina'}")
print(f"O preco que você irá pagar é de R${preco:.2f}")