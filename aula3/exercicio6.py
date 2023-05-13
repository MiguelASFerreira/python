"""
Crie um programa que pergunte ao usuário se ele é estudante 
e se tem menos de 18 anos. Se o usuário for estudante e tiver menos de 18 anos, 
imprima "Você tem direito à meia-entrada", caso contrário, 
imprima "Você não tem direito à meia-entrada".
"""

usuario = input("Você é estudante? (sim/não)").lower()
idade = int(input("Quantos anos você tem?"))

if (usuario == "sim" and idade < 18):
    print("Você tem direito à meia-entrada")
else:
    print("Você não tem direito à meia-entrada")