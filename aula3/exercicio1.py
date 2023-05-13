distancia = float(input("Digite a distância da pista? \n"))
velocidade1 = float(input("Digite a velocidade do carro 1? \n"))
velocidade2 = float(input("Digite a velocidade do carro 2? \n"))


posicao1 = 0
posicao2 = 0

while (posicao1 < distancia and posicao2 < distancia):
    posicao1 += velocidade1
    posicao2 += velocidade2

if (posicao1 > posicao2):
    print("O carro 1 venceu!")
elif (posicao2 > posicao1):
    print("O carro 2 venceu!")
else:
    print("Empate")