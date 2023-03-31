def ler_produtos():
    """
    Lê a entrada do usuário e cria uma lista de produtos.
    """
    produtos = []
    while True:
        entrada = input().strip()
        if not entrada:
            break
        codigo, descricao, quantidade, preco = entrada.split("#")
        produtos.append((codigo, descricao, int(quantidade), float(preco)))
    return produtos

def procurar_produto(codigo, produtos):
    """
    Procura um produto na lista de produtos por código.
    Retorna o produto encontrado ou None se não encontrado.
    """
    for produto in produtos:
        if produto[0] == codigo:
            return produto
    return None

# Programa principal
produtos = ler_produtos()

while True:
    codigo = input().strip()
    if not codigo:
        break
    produto = procurar_produto(codigo, produtos)
    if produto is None:
        print(f"Código {codigo} não localizado na lista de produtos!!!")
    else:
        print(f"Produto Localizado: {produto}")

print("Obrigado por utilizar nosso sistema!!!")
