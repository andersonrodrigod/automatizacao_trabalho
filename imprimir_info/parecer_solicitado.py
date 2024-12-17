import pandas as pd
 
df = pd.read_json("./dados/dados_coletados.json", encoding="utf-8")

palavra_chave = "PARECER"

grupo = "GRUPO"

info_assistente = df[df["info_assistente"].str.contains(palavra_chave, na=False)]

parecer = []

if not info_assistente.empty:
    
    if not grupo in info_assistente:
        for index, row in info_assistente.iterrows():
        
            solicitar_parecer = {
                "codigo": row["codigo"],
                "nome": row["nome"]
            }

            valores = list(solicitar_parecer.values())

            if not valores in parecer:
                parecer.append(valores)
            
        print(parecer)

    with open("parecers_solicitados", "w", encoding="utf-8") as arquivo_txt:
        for valor in parecer:
            arquivo_txt.write(f"{valor[0]} - {valor[1]}\n")

    
else:
    print("nenhum encontrado")