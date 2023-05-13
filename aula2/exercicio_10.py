items_pedido = {"Xbacon": 15, "Refri": 8, "Batata-frita": 5}

total_conta = 0

for item, valor in items_pedido.items():
    total_conta += valor
print(f"O valor total da compra é de R$ {total_conta:.2f}")