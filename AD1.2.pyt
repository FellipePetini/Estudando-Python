def ler_pessoas(n):
    pessoas = []
    for i in range(n):
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        peso = float(input("Digite o peso da pessoa: "))
        altura = float(input("Digite a altura da pessoa: "))
        pessoas.append((nome, idade, peso, altura))
    return pessoas

def listar_pessoas(pessoas, criterio):
    if criterio == 0:
        nome_primeira_pessoa = pessoas[0][0]
        pessoas_filtradas = [p for p in pessoas if p[0] > nome_primeira_pessoa]
    elif criterio == 1:
        idade_primeira_pessoa = pessoas[0][1]
        pessoas_filtradas = [p for p in pessoas if p[1] > idade_primeira_pessoa]
    elif criterio == 2:
        peso_primeira_pessoa = pessoas[0][2]
        pessoas_filtradas = [p for p in pessoas if p[2] > peso_primeira_pessoa]
    elif criterio == 3:
        altura_primeira_pessoa = pessoas[0][3]
        pessoas_filtradas = [p for p in pessoas if p[3] > altura_primeira_pessoa]
    else:
        raise ValueError("Criterio invalido")
    for pessoa in [pessoas[0]] + pessoas_filtradas:
        print(pessoa)

n = int(input("Digite a quantidade de pessoas: "))
pessoas = ler_pessoas(n)
criterio = int(input("Digite o criterio de listagem (0 - Ordenar por nome, 1 - Maior idade , 2 - Maior peso ou 3 - Maior Altura): "))
listar_pessoas(pessoas, criterio)
print("Obrigado por utilizar nosso sistema!!!")