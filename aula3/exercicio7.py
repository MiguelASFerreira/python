fumante = input("Você é fumante? (sim/nâo)\n").lower()
pressaoAlta = input("Você tem pressão alta? (sim/nâo)\n").lower()

if fumante == "sim" and pressaoAlta == "sim":
    print("Você precisa parar de fumar imediatamente!")
else:
    print("Parabéns por não fumar ou por manter sua pressão arterial controlada!")