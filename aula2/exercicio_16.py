media = 0
somaIdade = 0
nome_maisvelho = ""
idade_mulher = 0
counter = 0
maisVelho = 0

for i in range(1, 5):
    nome = str(input(f"Nome da {i}° pessoa?\n"))
    idade = int(input("Digite sua idade? \n"))
    sexo = str(input("Sexo [M/F]? \n")).upper

    if sexo == "M":
        if idade > maisVelho:
            maisVelho = idade
            nome_maisvelho = nome
    elif sexo == "F":
        if idade < 20:
            idade_mulher += 1
            
    counter+=1
    somaIdade+= idade
    media = (somaIdade/counter)

print("A média de idade do grupo é {}".format(media))
print("A idade do homem mais velho é {}".format(nome_maisvelho))

if idade_mulher == 0:
    print("Nenhuma mulher com menos de 20 anos")
elif idade_mulher == 1:
    print("{} mulher tem menos de 20 anos".format(idade_mulher))
elif idade_mulher >= 2:
    print("{} mulheres tem menos de 20 anos".format(idade_mulher))