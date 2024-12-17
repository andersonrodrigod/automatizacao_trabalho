import pandas as pd

df = pd.read_json("./dados/dados_coletados.json", encoding="utf-8")

palavra_chave = "PARECER"



info_medico = df[df["info_medico"].str.contains(palavra_chave, na=False)]

solicitar = []

if not info_medico.empty:

    for index, row in info_medico.iterrows():
        info_assistente = row["info_assistente"]
        if not palavra_chave in info_assistente:
            solicitar_parecer = {
                "codigo": row["codigo"],
                "nome": row["nome"]
            }
         

            valores = list(solicitar_parecer.values())

            if not valores in solicitar:
                solicitar.append(valores)
    
    with open("solicitar_parecer.txt", "w", encoding="utf-8") as arquivo_txt:
        for item in solicitar:
            arquivo_txt.write(f"{item[0]} - {item[1]}\n")

    
else:
    print("nao tem")