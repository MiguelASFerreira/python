nota1 = float(input("Digite a 1° nota: \n"))
nota2 = float(input("Digite a 2° nota: \n"))
media = (nota1 + nota2) / 2
print(f"A média desse aluno é {media}")
if (media == 10):
    print("Aprovado com Louvor")
elif (media >= 7):
    print("Aprovado")
else:
    print("Reprovado")