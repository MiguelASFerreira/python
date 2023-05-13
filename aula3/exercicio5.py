vegetariano = input("Você é vegetariano? (sim/não)\n").lower()
gluten = input("Você é alérgico a glúten? (sim/não)\n").lower()

if vegetariano == "sim" and gluten == "sim":
    print("Você pode comer no restaurante X")
else:
    print("Você não pode comer no restaurante X")