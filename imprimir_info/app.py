from processamento_texto import processar_dados_por_nome
import pandas as pd


df = pd.read_json("./dados/dados_coletados.json", encoding="utf-8")

nome = "ARACELLY APARECIDA DOS SANTOS SILVA"

resultado = processar_dados_por_nome(df, nome)

for chave, valor in resultado.items():
    if valor is not None:
        print(f"{valor}\n")