import math

def ler_pontos(arquivo):
    pontos = []
    with open(arquivo, "r") as f:
        for linha in f:
            coordenadas = linha.split()
            if len(coordenadas) != 3:
                print("Erro: É necessário informar 3 coordenadas (x, y, z) separadas por espaço.")
                continue
            try:
                x = int(coordenadas[0])
                y = int(coordenadas[1])
                z = int(coordenadas[2])
                pontos.append((x, y, z))
            except ValueError:
                print("Erro: As coordenadas devem ser números inteiros.")
    return pontos

def ler_esfera():
    linha = input("Digite as coordenadas x, y e z do centro da esfera, seguidas do raio, separadas por espaço: ")
    coordenadas = linha.split()
    if len(coordenadas) != 4:
        print("Erro: É necessário informar 4 coordenadas (x, y, z, raio) separadas por espaço.")
        return None
    try:
        x = int(coordenadas[0])
        y = int(coordenadas[1])
        z = int(coordenadas[2])
        raio = int(coordenadas[3])
        return (x, y, z, raio)
    except ValueError:
        print("Erro: As coordenadas e o raio devem ser números inteiros.")
        return None

def calcular_distancia(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distancia

def pontos_dentro_da_esfera(pontos, centro, raio):
    pontos_dentro = []
    for ponto in pontos:
        if calcular_distancia(ponto, centro) <= raio:
            pontos_dentro.append(ponto)
    return pontos_dentro

def main():
    # Leitura do arquivo de pontos
    arquivo = input("Digite o caminho do arquivo de pontos: ")
    try:
        pontos = ler_pontos(arquivo)
    except FileNotFoundError:
        print("Erro: O arquivo de pontos não existe ou não pode ser aberto.")
        return
    if len(pontos) == 0:
        print("Nenhum ponto foi lido - O arquivo estava vazio!!!")
        return

    # Leitura da esfera
    centro_raio = ler_esfera()
    if centro_raio is None:
        return
    centro, raio = centro_raio

    # Listagem dos pontos lidos
    print("Pontos lidos:")
    for ponto in pontos:
        print(ponto)

    # Listagem dos pontos dentro da esfera
    pontos_dentro = pontos_dentro_da_esfera(pontos, centro, raio)
    print("Pontos dentro da esfera:")
    for ponto in pontos_dentro:
        print(ponto)

if __name__ == '__main__':
    main()