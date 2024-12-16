import pandas as pd


df = pd.read_json("./dados/dados_coletados.json", encoding="utf-8")

nome_select = "RAFAELA DE SOUSA SARAIVA"

linha = df[df["nome"] == nome_select]

if not linha.empty:

    for index, row in linha.iterrows():
        codigo = row["codigo"]
        nome = row["nome"]
        info_assistente = row["info_assistente"]
        info_medico = row["info_medico"]

        print(f"Informações do usuário {nome}:")
        print(f"Codigo: {codigo}")
        print(f"Info Médico: {info_medico}")
        print(f"Info Assistente: {info_assistente}")
else:
    print("nome não encontrado")






