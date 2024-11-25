import pyautogui as py
import customtkinter as ctk
import os
import json
from tkinter import messagebox



def enviar():
    if not codigo.get() or not nome.get():
        messagebox.showerror("Erro", "Código e Nome são obrigatórios.")
        return
    
    novo_procedimento = {
        "cod_proce": cod_proc.get(),
        "nome_proce": nome_proc.get(),
        "texto_user": texto_usuario.get(),
        "texto_med": texto_medico.get(),
        "id_proce": 1
    }

    dados = {
        "cod": codigo.get(),
        "name": nome.get(),
        "procedimentos": [novo_procedimento]
    }

    arquivo_json = "dados.json"

    # Criar o arquivo JSON se não existir
    if not os.path.exists(arquivo_json):
        with open(arquivo_json, "w", encoding="utf-8") as arquivo: 
            json.dump([], arquivo)

    # Ler o conteúdo existente
    with open(arquivo_json, "r", encoding="utf-8") as arquivo:
        conteudo_existente = json.load(arquivo)

    # Verificar se já existe o mesmo código e nome
    for item in conteudo_existente:
        if item["cod"] == dados["cod"] and item["name"] == dados["name"]:
            # Incrementar ID e adicionar novo procedimento
            novo_procedimento["id_proce"] = len(item["procedimentos"]) + 1
            item["procedimentos"].append(novo_procedimento)
            break
    else:
        # Adicionar um novo registro completo
        conteudo_existente.append(dados)
    
    # Salvar os dados no arquivo
    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(conteudo_existente, arquivo, indent=4, ensure_ascii=False)

    # Limpar os campos
    codigo.delete(0, 'end')
    nome.delete(0, 'end')
    cod_proc.delete(0, 'end')
    nome_proc.delete(0, 'end')
    texto_usuario.delete(0, 'end')
    texto_medico.delete(0, 'end')



janela = ctk.CTk()


janela.title("Armazenamento SPE")
janela.geometry("600x400")
janela.resizable(width=False, height=False)

cod_label = ctk.CTkLabel(janela, text="Código")
cod_label.pack()
codigo = ctk.CTkEntry(janela, width=200)
codigo.pack()

nome_label = ctk.CTkLabel(janela, text="Nome")
nome_label.pack()
nome = ctk.CTkEntry(janela, width=400)
nome.pack()

cod_proc_label = ctk.CTkLabel(janela, text="Código do Procedimento")
cod_proc_label.pack()
cod_proc = ctk.CTkEntry(janela, width=100)
cod_proc.pack()

nome_proc_label = ctk.CTkLabel(janela, text="Nome do Procedimento")
nome_proc_label.pack()
nome_proc = ctk.CTkEntry(janela, width=400)
nome_proc.pack()

texto_usuario_label = ctk.CTkLabel(janela, text="Atualização Pré-Existencia")
texto_usuario_label.pack()
texto_usuario = ctk.CTkEntry(janela, width=400)
texto_usuario.pack()

texto_medico_label = ctk.CTkLabel(janela, text="Atualização Médica")
texto_medico_label.pack()
texto_medico = ctk.CTkEntry(janela, width=400)
texto_medico.pack()

btn_enviar = ctk.CTkButton(janela, text="Enviar", command=enviar)

btn_enviar.pack(pady=10)





janela.mainloop()

