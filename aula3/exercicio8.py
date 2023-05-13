idade = int(input("Digite sua idade?\n"))
inssAnos = int(input("Quantos anos de contribuição vcê tem ao INSS?\n"))
if idade >= 60 or inssAnos >= 30:
    print("Pode se aposentar!")
else:
    print("Não pode aposentar!")
