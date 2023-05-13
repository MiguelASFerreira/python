import os
os.system("cls")
print("------------------------------")
def lerDados():
    nome = input("Digite seu nome? ")
    idade = int(input("Digite sua idade? "))
    print("O seu nome é {0}, e sua idade é {1}".format(nome, idade))
    print("-----------------------------")
    resposta = input("Deseja continuar? S/N ")
    if (resposta.upper() == "S"): 
        lerDados()  

    

print("Digite seus dados")
lerDados()