'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz
um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por
quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso
a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''
while True:
 peso = float(input("Quantos quilos foram feitos hoje? :"))

 if peso > 50: 
    excesso = peso - 50
    multa = excesso * 4.00 

 else: 
    excesso = 0
    multa = 0

 print("Peso de peixes: %.2f kg" % peso)
 if excesso > 0: 
   print("Excesso de peso: %.2f kg" % excesso)
   print("Multa a pagar: R$ %.2f" % multa)

 else:
     print("Não houve excesso de peso. Multa: R$0,00")


 continuar = input("Deseja continuar? (s/n): ")
 if continuar.lower() != "s" :
  break

