# Elaborar um algoritmo que solicita 4 notas ao usuário.
# O progrma de calcular a média das notas e 
# verificar se a média é maior ou igual a 80, o programa 
# deve exibir a mensagem "aprovado" e se a média for menor que 
# 80, o programa deve exibir a mensagem "Reprovado"

nota1 = float(input("Digite a nota 1:"))
nota2 = float(input ("Digite a nota 2:"))
nota3 = float(input ("Digite a nota 3:"))
nota4 = float(input ("Digite a nota 4:"))

media = (nota1 + nota2 + nota3+ nota4) / 4 
print(f"A média final obtida = {media}")

if (media >=80):
    print("Aprovado")
else: 
    print("Reprovado")