import os
os.system("cls")
print("---------------------------")
nome = input("Digite seu nome? ")
idade = input("Digite sua idade? ")
print("Nome: ",nome)
print("Idade: ",idade," anos")
idade = int(idade)
dias = idade * 365
print("Já viveu:",dias, "dias")
print("----------------------------")