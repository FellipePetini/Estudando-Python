#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7


altura = input("Você é homem ou mulher?: ")

if altura.lower() == "homem":
  alturah = float(input("Digite sua altura:"))
  pesohomem = (72.7*alturah) - 58
  pesohomem = round(pesohomem, 2)
  print("Seu peso ideal e de:", pesohomem)

elif altura.lower() == "mulher" : 
   alturam = float(input("Digite sua altura:"))
   pesomulher = (62*alturam) - 44.7
   pesomulher = round(pesomulher, 2)
   print("Seu peso idealé de:", pesomulher)

else:
   print("Porfavor , insira 'homem' ou 'mulher. ")


