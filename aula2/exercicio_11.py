transacoes = {100,-50,300,-200,50}
saldo = 0

for transacao in transacoes:
    saldo += transacao
print(f"O salado da conta é de R$ {saldo:.2f}")