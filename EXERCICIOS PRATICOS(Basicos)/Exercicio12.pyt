#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Para descobrir seu peso ideal primeiro me de sua altura: "))

pesoideal = (72.7*altura) - 58
pesoideal = round(pesoideal, 2)

print("Seu peso ideal e", pesoideal)


