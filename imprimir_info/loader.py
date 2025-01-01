import pandas as pd
from tkinter import filedialog, messagebox
import os
import json


def filtrar_nome(df, nome):
    return df[df["nome"] == nome].drop_duplicates(subset="nome", keep="first")


def carregar_arquivo_json(caminho_arquivo=None):

    if not caminho_arquivo:
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione um arquivo JSON",
            filetypes=[("Arquivos JSON", "*.json")]
        )

    if caminho_arquivo:
        try:
            df = pd.read_json(caminho_arquivo)
            messagebox.showinfo("Sucesso", "Arquivo JSON carregado com sucesso")
            if df is not None:
                return df, caminho_arquivo
            else:
                print("Nenhum dado foi carregado")
                return None, caminho_arquivo
            
        except ValueError as e:
            messagebox.showerror("Erro", f"Erro ao ler o arquivo JSON:\n{e}")
        except Exception as e:
            messagebox.showerror("Erro", "invesperado: \n{e}")

    else:
        messagebox.showwarning("Aviso", "Nenhum arquivo foi selecionado")

        return None, None
    


def criar_arquivo():
    caminho_do_arquivo = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", ".json"), ("All files", ".")],
        title="Salvar arquivo"
    )

    posicao = {
        "codigo_carteira": [
            {"x": 0, "y": 0}
        ],
        "info_meidico" : [
            {"x": 0, "y": 0}
        ],
        "info_assistente": [
            {"x": 0, "y": 0}
        ]
    }

    if caminho_do_arquivo:
        with open(caminho_do_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(posicao, arquivo, indent=4)
            print(f"arquivo {caminho_do_arquivo} criado com sucesso")       
   
        


def carregar_arquivo(caminho_do_arquivo):
    with open(caminho_do_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        
    print(f"Arquivo {caminho_do_arquivo}, carregado com sucesso")
    return dados