positivos = 0
resposta1 = input("Telefonou para a vítima? (S ou N)\n").upper()
if resposta1 == "S":
    positivos += 1
resposta2 = input("Esteve no local do crime? (S ou N)\n").upper()
if resposta2 == "S":
    positivos += 1
resposta3 = input("Mora perto da vítima? (S ou N)\n").upper()
if resposta3 == "S":
    positivos += 1
resposta4 = input("Devia para a vítima? (S ou N)\n").upper()
if resposta4 == "S":
    positivos += 1
resposta5 = input("Já trabalhou com a vítima? (S ou N)\n").upper()
if resposta5 == "S":
    positivos += 1

print(f"Contador: {positivos}")

if positivos < 2:
    print("Inocente")
elif positivos == 2:
    print("Suspeito")
elif positivos < 5:
    print("Cúmplice")
else:
    print("Assassino")