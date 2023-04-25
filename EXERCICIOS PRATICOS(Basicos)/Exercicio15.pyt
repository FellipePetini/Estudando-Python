'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
A= salário bruto.
B= quanto pagou ao INSS.
C= quanto pagou ao sindicato.
D= o salário líquido.
E= calcule os descontos e o salário líquido

+ Salário Bruto : R$ - IR (11%) : R$ - INSS (8%) : R$ - Sindicato ( 5%) : R$ = Salário Liquido : R$

'''
while True:
 Ghoras = float(input("Quanto você ganha por hora?: "))
 if Ghoras <= 0:
        print("Erro!! O numero colocado é igual ou menor que 0  ")
 else:
        break

while True:
 Nhoras = float(input("Quantas horas você trabalha/ou no mês?: "))
 if Nhoras <= 0:
        print("Erro!! O numero colocado não funciona ")
 else:
        break

A = Ghoras * Nhoras 
B = A * (8/100)
C = A * (5/100)
F = A * (11/100)
D = (B - C - ( F )) + A


Resultado = """
{}
O calculo com os desconto mais o salário líquido ficou desta forma: 
# Salário Bruto : R${:.2f}
# IR (11%) : R${:.2f}
# INSS (8%) : R${:.2f}
# Sindicato (5%) : R${:.2f}
# Salário Liquido : R${:.2f}
{}
""".format("-"*100,A, F, B, C, D,"-"*100)

print(Resultado)



