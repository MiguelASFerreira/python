nome = input("Digite o seu nome? \n").upper()

if (nome == "LUCAS" or nome == "PEDRO"):
    print(f"{nome} é um admin. Bem-Vindo!")
else:
    print(f"{nome} não é um admin. Bem-Vindo!")