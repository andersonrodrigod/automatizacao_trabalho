import pandas as pd


def trocar_virgula():
    separador = " - "
    with open("solicitar_parecer.txt", "r", encoding="utf-8") as arquivo:
        content = arquivo.read()
        content = content.replace(",", separador)

    with open("solicitar_parecer.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(content)


df = pd.read_json("./dados/dados_coletados.json", encoding="utf-8")

parecer = "PARECER"
grupo = "GRUPO"
separador = " - "


filtrar_parecer = df["info_assistente"].str.contains(parecer, na=False)
filtrar_grupo = ~df["info_assistente"].str.contains(grupo, na=False)

resultado = df[filtrar_parecer & filtrar_grupo]

resultado = resultado[["codigo", "nome"]].drop_duplicates()


if not resultado.empty:
    print(resultado)

    resultado.to_csv("solicitar_parecer.txt", sep=",", index=False, header=False, encoding="utf-8")
    trocar_virgula()
else:
    print("nenhum encontrado")