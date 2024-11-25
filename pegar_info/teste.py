import pandas as pd
import os



dados = ["3010J859856785", "ANDERSON RODRIGO RODRIGUES DOS SANTOS", "23852854", "LAPAROSCOPIA", "DS SOLICITADA", "SOLICTAR DS"]


def save_create():

    file_path = "teste.xlsx"

    collumns= ["Codigo da Carteirinha", "Nome", "Codigo do Procedimento", "Nome do Procedimento", "Informacao do Usuario", "Informacao Medica", "Telefone" ]

    while len(dados) < len(collumns):
        dados.append(None)
        
    df = pd.DataFrame([dados], columns=collumns)

    if os.path.exists(file_path):
        
        existing_df = pd.read_excel(file_path)

        update_df = pd.concat([existing_df, df], ignore_index=True)

        update_df.to_excel(file_path, index=False)
        print("Arquivo subscrito com sucesso")
    else:
        
        df.to_excel(file_path, index=False)
        print("arquivo criado com sucesso")




save_create()