#Um programa que simule o jogo de adivinhação, 
#em que o usuário deve tentar adivinhar um número escolhido pelo programa. 
#O programa deve informar ao usuário se o número digitado
#é maior ou menor do que o número escolhido. 
#O jogo deve continuar até que o usuário acerte o número escolhido.
import random
escolhido = random.randint(1, 100)
print(escolhido)
tentativa = 1

print(">>>>>>>>>>>>Jogo de Adivinhação<<<<<<<<<<<<<")
print(">>>>>>>>>>>>De 1 à 100<<<<<<<<<<<<<")
resposta = int(input(f"Digite {tentativa}° número? \n"))

if (resposta == escolhido):
    print("Você acertou em", tentativa, "tentaiva(s). O número era", escolhido)
tentativa += 1


while (resposta != escolhido):
    resposta = int(input(f"Digite {tentativa}° número? \n"))
    if (resposta == escolhido):
        print("Você acertou em", tentativa, "tentaiva(s). O número era", escolhido)
        break

    if (tentativa == 5):
        if (escolhido % 2 == 0):
            print("\nÉ um número Par!\n")
        else:
            print("\nÉ um número Ímpar!\n")

    if (tentativa == 10):
        if (escolhido > 0 and escolhido <= 20):
            print("\nO número é maior ou igual a 1 e menor ou igual a 20\n")
        else:
            print("\nO número é maior que 20\n")
    
    if (tentativa == 15):
        if (escolhido > 20 and escolhido <= 40):
            print("\nO número é maior a 20 e menor ou igual a 40\n")
        elif (escolhido > 40 and escolhido <= 60):
            print("\nO número é maior a 40 e menor ou igual a 60\n")
    
    if (tentativa == 20):
        if (escolhido > 60 and escolhido <= 80):
            print("\nO número é maior a 60 e menor ou igual a 80\n")
        elif (escolhido > 80):
            print("\nO número é maior que 80\n")

    tentativa += 1


    