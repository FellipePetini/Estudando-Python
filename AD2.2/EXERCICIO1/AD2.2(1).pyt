import struct

def ler_registros():
    try:
        with open("cliente.bin", "rb") as arquivo:
            while True:
                registro = arquivo.read(170)
                if not registro:
                    break
                pais, cidade, aeroporto, cias = struct.unpack("10s40s40s80s", registro)
                yield pais.decode("utf-8").strip(), cidade.decode("utf-8").strip(), aeroporto.decode("utf-8").strip(), cias.decode("utf-8").strip().split("&")
    except FileNotFoundError:
        return None

def consulta_pais(nome_pais):
    aeroportos = []
    for pais, cidade, aeroporto, cias in ler_registros():
        if pais == nome_pais:
            aeroportos.append((aeroporto, cidade))
    if not aeroportos:
        return f"'{nome_pais}' não é um país listado na nossa base."
    return f"{len(aeroportos)} aeroportos encontrados:\n" + "\n".join(f"{aeroporto}, {cidade}" for aeroporto, cidade in aeroportos)

def consulta_aeroporto(nome_aeroporto):
    cias = []
    for pais, cidade, aeroporto, cias_aereas in ler_registros():
        if aeroporto == nome_aeroporto:
            cias.extend(cias_aereas)
    if not cias:
        return f"O aeroporto '{nome_aeroporto}' não está na nossa base."
    return f"{len(cias)} cias. aéreas operam no aeroporto '{nome_aeroporto}':\n" + "\n".join(cias)

def consulta_cia(nome_cia):
    aeroportos = []
    for pais, cidade, aeroporto, cias_aereas in ler_registros():
        if nome_cia in cias_aereas:
            aeroportos.append((aeroporto, cidade, pais))
    if not aeroportos:
        return f"A companhia aérea '{nome_cia}' não opera para nenhum dos aeroportos da base ou digitou errado."
    return f"A companhia aérea '{nome_cia}' opera em {len(aeroportos)} aeroportos:\n" + "\n".join(f"{aeroporto}, {cidade}, {pais}" for aeroporto, cidade, pais in aeroportos)

def consulta(tipo_consulta, nome_consulta):
    if tipo_consulta == "país":
        return consulta_pais(nome_consulta)
    elif tipo_consulta == "aeroporto":
        return consulta_aeroporto(nome_consulta)
    elif tipo_consulta == "cia":
        return consulta_cia(nome_consulta)
    else:
        return "Tipo de consulta inválido."

tipo_consulta = input("Digite o tipo de consulta (país, aeroporto ou cia): ")
nome_consulta = input("Digite o nome a ser consultado: ")

resultado = consulta(tipo_consulta, nome_consulta)
if resultado is None:
    print("Um dos arquivos não foi encontrado ou digitou errado.")
else:
    print(resultado)
