morango = float(input("Digite quanyos quilos de morango foram comprados? \n"))
maca = float(input("Digite quanyos quilos de maça foram comprados? \n"))

valor = 0

if (morango <= 5):
    valor += morango * 2.5
else:
    valor += morango * 2.2

if (maca <= 5):
    valor += maca * 1.8
else:
    valor += maca * 1.5

print(f"Valor: {valor:.2f}")

if ((morango + maca) > 8 or valor > 25):
    valor -= valor * 10/100

print(f"Valor Final da compra: {valor:.2f}")