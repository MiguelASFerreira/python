senhaUsuario = "12c4"
tentativa = 0

while (tentativa < 3):
    senha = input("Digite sua senha? \n")
    if (senha == senhaUsuario):
        print("Bem-Vindo")
        break
    print("Senha incorreta!")  
    tentativa = tentativa + 1 
    
if (tentativa == 3):
    print("Bloqueando o usuário")
