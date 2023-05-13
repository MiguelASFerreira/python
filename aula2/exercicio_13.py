produtos_promocao = {"Camiseta", "Calça", "Tênis"}
percentual_desconto = 30
preco_original = 100

for produto in produtos_promocao:
    preco = preco_original + (preco_original + (percentual_desconto/100))
    print(f"{produto} tem um desconto de {percentual_desconto}%. De R$ {preco_original} por R$ {preco}")