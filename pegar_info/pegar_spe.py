import pyautogui as py
import customtkinter as ctk


janela = ctk.CTk()


janela.title("Armazenamento SPE")
janela.geometry("600x370")
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

btn_enviar = ctk.CTkButton(janela, text="Enviar")





janela.mainloop()

