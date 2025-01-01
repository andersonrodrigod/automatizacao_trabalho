from execucao_texto import processar_dados_por_nome 
from processar_texto import texto_solicitacao
from loader import carregar_arquivo_json, criar_arquivo
from coletar_dados import save_data
import pandas as pd
import customtkinter as ctk
from tkinter import messagebox
import mouseinfo
from tkinter import filedialog
import json



class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(size)

        self.df = None
        self.caminho = None
        
        
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=333)
        self.grid_columnconfigure(1, weight=1, minsize=333)
        self.grid_columnconfigure(2, weight=1, minsize=333)

        self.formatar_texto = Formatar_texto(self) 
        self.menu = Menu(self, self.formatar_texto) 
        self.carregar = Carregar(self, self.menu, self)
        """self.carregar.grid(row=0, column=0, columnspan=3, sticky="nsew")"""
        """self.formatar_texto.grid(row=0, column=0, columnspan=3, sticky="nsew")"""
        self.menu.grid(row=0, column=0, columnspan=3, sticky="nsew")
        


class Carregar(ctk.CTkFrame):
    def __init__(self, parent, menu, app):
        super().__init__(parent)

        self.menu = menu 
        self.app = app 

        self.grid_columnconfigure(0, weight=1, minsize=330)
        self.grid_columnconfigure(1, weight=1, minsize=330)
        self.grid_columnconfigure(2, weight=1, minsize=330)

        self.label_info_inicial = ctk.CTkLabel(self, text="Carregue um arquivo para executar")
        self.label_info_inicial.grid(row=0, column=1, pady=15, padx=(0, 0))

        self.btn_carregar_arquivo = ctk.CTkButton(self, text="Carregar Arquivo", 
        command=self.carregar_dados)
        self.btn_carregar_arquivo.grid(row=1, column=1, pady=15, padx=(10, 0))

    def carregar_dados(self):
        df, caminho = carregar_arquivo_json()
        if df is not None:
            self.app.df = df
            self.app.caminho = caminho
            self.grid_forget()
            self.menu.grid(row=0, column=0, columnspan=3, sticky="nsew")   
            return df
        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo foi carregado corretamente.")
        return df

class Menu(ctk.CTkFrame):
    def __init__(self, parent, formatar_texto):
        super().__init__(parent)

        self.formatar_texto = formatar_texto 
        self.parent = parent

        self.posicao = {
            "codigo_carteira": [{"x": 0, "y": 0}],
            "info_meidico": [{"x": 0, "y": 0}],
            "info_assistente": [{"x": 0, "y": 0}]
        }

        self.grid_columnconfigure(0, weight=1, minsize=330)
        self.grid_columnconfigure(1, weight=1, minsize=330)
        self.grid_columnconfigure(2, weight=1, minsize=330)

        self.label_menu = ctk.CTkLabel(self, text="MENU DE OPÇÕES")
        self.label_menu.grid(row=0, column=1, pady=15, padx=(1, 1))

        self.btn_formatar_texto = ctk.CTkButton(self, text="Formatar Texto", width=250, command=self.exibir_formatar_texto)
        self.btn_formatar_texto.grid(row=1, column=1, pady=(10,0), padx=(1, 1))

        self.btn_buscar_localização = ctk.CTkButton(self, text="Buscar Localização", width=250, command=self.mouse_info)
        self.btn_buscar_localização.grid(row=2, column=1, pady=(5,0), padx=(1, 1))

        self.btn_registrar_posicao = ctk.CTkButton(self, text="Registrar Posição", width=250, command=self.abrir_nova_janela)
        self.btn_registrar_posicao.grid(row=3, column=1, pady=(5, 800), padx=(1, 1))

    def exibir_formatar_texto(self):
        self.grid_forget()
        self.formatar_texto.grid(row=0, column=0, columnspan=3, sticky="nsew")

    def mouse_info(self):
        mouseinfo.MouseInfoWindow()

    def abrir_nova_janela(self):
        self.nova_janela = ctk.CTkToplevel(self.parent)
        self.nova_janela.title("Registrar Posição")
        self.nova_janela.geometry("400x100")
        self.nova_janela.grab_set()

        self.nova_janela.grid_columnconfigure(0, weight=1, minsize=200)
        self.nova_janela.grid_columnconfigure(1, weight=1, minsize=200)

     
        label = ctk.CTkLabel(self.nova_janela, text="Preencha as coordenadas:", font=("Arial", 16))
        label.grid(row=0, column=0, pady=5, padx=5, columnspan=2, sticky="nsew")

        botao1 = ctk.CTkButton(self.nova_janela, text="Criar Arquivo", command=self.criar_arquivo)
        botao1.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")

        botao2 = ctk.CTkButton(self.nova_janela, text="Carregar Arquivo", command=lambda: print("Opção 2 selecionada"))
        botao2.grid(row=1, column=1, pady=5, padx=5, sticky="nsew")

class Formatar_texto(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.grid_columnconfigure(0, weight=1, minsize=200)
        self.grid_columnconfigure(1, weight=3, minsize=600)
        self.grid_columnconfigure(2, weight=1, minsize=200)

        # ==== Coluna 0 (com Frame para Botões) ====
        self.frame_coluna0 = ctk.CTkFrame(self)
        self.frame_coluna0.grid(row=0, column=0, sticky="nw", padx=10, pady=5)

        self.btn_coletar_dados = ctk.CTkButton(self.frame_coluna0, text="Coletar Dados", command=self.quantidade_coletar_dados)
        self.btn_coletar_dados.grid(row=0, column=0, pady=(5, 5), padx=(10, 10), sticky="w")

        self.btn_enviar_erro = ctk.CTkButton(self.frame_coluna0, text="Enviar Erro")
        self.btn_enviar_erro.grid(row=1, column=0, pady=(5, 5),  padx=(10, 10), sticky="w")

        self.btn_enviar_ = ctk.CTkButton(self.frame_coluna0, text="Enviar Erro")
        self.btn_enviar_.grid(row=2, column=0, pady=(5, 5),  padx=(10, 10), sticky="w")

         # ==== Coluna 1 (com Frame para Botões) ====
        self.frame_coluna1 = ctk.CTkFrame(self)
        self.frame_coluna1.grid(row=0, column=1, padx=(5, 5), pady=10, sticky="nw")
        
        self.label_title = ctk.CTkLabel(self.frame_coluna1, text="Formatação de Texto", width=600)
        self.label_title.grid(row=0, column=1, pady=15, padx=(1, 1))

        self.label_nome = ctk.CTkLabel(self.frame_coluna1, text="Nome: ", width=50)
        self.label_nome.grid(row=2, column=1, pady=15, padx=(1, 1), sticky="w")

        self.input_nome = ctk.CTkEntry(self.frame_coluna1, placeholder_text="Digite o Nome", width=530)
        self.input_nome.grid(row=2, column=1, padx=(0, 20), sticky="e")

        self.textarea_texto = ctk.CTkTextbox(self.frame_coluna1, height=300, width=570)
        self.textarea_texto.grid(row=3, column=1, padx=(10, 20))

        self.btn_enviar = ctk.CTkButton(self.frame_coluna1, text="Formatar", width=400, height=35, command=self.organizar_texto)
        self.btn_enviar.grid(row=4, column=1, pady=(15, 500))
  
    def organizar_texto(self):
        nome_digitado = self.input_nome.get()
        df = self.parent.df
        if df is not None:
            resultado = processar_dados_por_nome(df, nome_digitado)
            resultado = texto_solicitacao(resultado)
            self.textarea_texto.delete('0.0', 'end')
            self.textarea_texto.insert('0.0', f'{resultado}')
        else:
            print("nenhum dado carregado")
  
    def quantidade_coletar_dados(self):
        dialog = ctk.CTkInputDialog(title="Número de Coletas", text="Digite o número de coletas")

        try:
            quantidade_str = dialog.get_input()
            if quantidade_str is None or quantidade_str.strip() == "":
                raise ValueError("Nenhum valor foi inserido")

            quantidade = int(quantidade_str)

            print(f"Tipo: {type(quantidade)}, Valor: {quantidade}")

            if quantidade <= 0:
                raise ValueError("O número deve ser maior que zero")

            print("Chamando coletar_dados...")
            self.coletar_dados(quantidade)
            print("Dados coletados com sucesso!")

        except (ValueError, TypeError):
            messagebox.showerror("Erro", "Por favor, insira um número inteiro válido.")

    def coletar_dados(self, quantidade):
        try:
            caminho = self.parent.caminho
            print(f"Coletando {quantidade} dados no caminho: {caminho}")
            for i in range(quantidade):

                print(f"Coleta {i+1} de {quantidade}")
                dados = save_data(caminho)
                print(f"Dado coletado: {dados}")
        except Exception as e:
            print(f"Erro em coletar_dados: {e}")
        import traceback
        traceback.print_exc()
            


if __name__ == "__main__":
    app = App("Salvando sua vida", "1000x700")
    app.mainloop()



