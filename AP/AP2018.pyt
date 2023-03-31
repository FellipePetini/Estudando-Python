def inverte_palavras(frase):
    palavras = frase.split()
    nova_frase = ''
    for palavra in palavras:
        num_vogais = sum(1 for letra in palavra if letra in 'aeiouAEIOU')
        if num_vogais % 2 == 1:
            nova_frase += palavra[::-1] + ' '
        else:
            nova_frase += palavra + ' '
    return nova_frase.strip()

while True:
    entrada = input("Digite uma frase: ")
    if not entrada:
        break
    saida = inverte_palavras(entrada)
    print("Frase invertida: " + saida)