def contagem_votos():
    contagem = {}
    while True:
        entrada = input("Insira o número do candidato (0 a 9): ")
        if not entrada: 
            break
        voto = int(entrada)
        if voto < 0 or voto > 9:
            print("Número de candidato inválido!")
            continue
        if voto in contagem:
            contagem[voto] += 1
        else:
            contagem[voto] = 1
    return contagem

votos = contagem_votos()

if not votos:
    print("Nenhum voto ocorreu!!!")
else:
    for candidato, contagem in votos.items():
        print(f"Candidato {candidato}: {contagem} votos")
