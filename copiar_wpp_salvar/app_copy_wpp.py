import customtkinter as ctk
import pyautogui as py
import time
import pyperclip
import tkinter.filedialog as fd
import os
from tkinter import messagebox

janela = ctk.CTk()
janela.title("SALVAR IMAGEM DO WHATS APP")
janela.geometry("700x400")
janela.minsize(width=700, height=350)
janela.maxsize(width=700, height=350)
janela.resizable(width=False, height=False)
janela.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
janela.grid_columnconfigure(0, weight=1, minsize=140)
janela.grid_columnconfigure(1, weight=1, minsize=140)
janela.grid_columnconfigure(2, weight=2, minsize=140) 
janela.grid_columnconfigure(3, weight=1, minsize=140)
janela.grid_columnconfigure(4, weight=0, minsize=140)

largura, altura = py.size()
diretorio_salvar = ""
x = largura / 2
y = altura / 2

def corrigir_caminho(caminho):
    return os.path.normpath(caminho)

def novidades_breve():
    try:
        messagebox.showerror("Acalma o coração 😜", "Novidades em Breve.")
        return
    except ValueError as e:
        print(f"Erro capturado: {e}")

def copiar_wpp():
    py.click(x, y, button="right")
    for _ in range(3):
        py.press("down")
    time.sleep(1)
    py.press("enter")
    time.sleep(0.2)

def abrir_paint():
    if not diretorio_salvar:
        print("Erro: Diretório de salvamento não foi definido.")
        return
    
    py.hotkey("win", "d")
    time.sleep(1)
    os.system("start mspaint")
    time.sleep(0.5)

def colar_img():
    py.click(x, y) 
    time.sleep(0.5)
    py.hotkey("ctrl", "v")
    time.sleep(0.5)

def salvar_img(count):
    py.press("alt")
    time.sleep(0.5)
    py.press("f")
    time.sleep(0.5)
    for _ in range(3):
        time.sleep(0.1)
        py.press("down")
    py.press("right")
    time.sleep(0.5)
    py.press("j")
    time.sleep(0.5)
    py.hotkey("ctrl", "l")
    time.sleep(0.5)
    pyperclip.copy(diretorio_salvar)
    time.sleep(0.5)
    py.hotkey("ctrl", "v")
    time.sleep(0.5)
    py.press("enter")
    time.sleep(0.5)
    py.hotkey("ctrl", "l")
    time.sleep(0.5)
    py.press("enter")
    time.sleep(0.5)
    py.hotkey("shift", "tab")
    time.sleep(0.5)
    py.hotkey("shift", "tab")
    time.sleep(0.5)
    py.click(355, 396)
    count_str = str(count)
    py.write(count_str, interval=0.5)
    py.press("enter")
    time.sleep(0.5)
    py.hotkey("alt", "f4")
    time.sleep(1)

def proxima_imagem():
    py.hotkey("alt", 'tab')
    time.sleep(1)
    py.press("right")
    time.sleep(1)

def minimizar():
    # Minimiza a janela
    janela.iconify()
    
def salvando_imgs_wpp(quantidade_valor):
    count = 1
    time.sleep(3)
    for _ in range(quantidade_valor):
        copiar_wpp()
        abrir_paint()
        colar_img()
        salvar_img(count)
        proxima_imagem()
        count += 1
    print("processo concluído")

def executar_tarefa():
    global quantidade
    if not diretorio_salvar:
        messagebox.showerror("Ta com pressa? 🏃‍♀️ Calma, não é corrida!", "Por favor, selecione um diretório para salvar os arquivos.")
        return

    try:
        quantidade_valor = int(quantidade.get().strip())
        
        if quantidade_valor <= 0:
            messagebox.showerror("Você tá de palhaçada! 🤡, Zero a esquerda!", "A quantidade deve ser um número positivo.      ")
            return
    except ValueError:
        messagebox.showerror("Tá achando que é mágica?🎩 Não dá pra fazer sem o número!", "Por favor, insira um número válido para a quantidade.        ")
        return

    minimizar()
    salvando_imgs_wpp(quantidade_valor)
    
def escolher_diretorio():
    global diretorio_salvar
    diretorio_salvar = fd.askdirectory()
    if diretorio_salvar:
        diretorio_salvar = corrigir_caminho(diretorio_salvar)
        label_diretorio.configure(text=f"Diretório: {diretorio_salvar}")

def somente_numeros(text):
    return text.isdigit()

configurações = ctk.CTkButton(janela, text="Configurações", width=100, command=novidades_breve)
configurações.grid(row=0, column=4, pady=10, padx=(0, 5), sticky="e")

label_diretorio = ctk.CTkLabel(janela, text="Diretório: Não definido", wraplength=650)
label_diretorio.grid(row=1, column=1, columnspan=3, pady=(30, 10))

btn_escolher_diretorio = ctk.CTkButton(janela, text="Escolher Diretório", command=escolher_diretorio, width=140)
btn_escolher_diretorio.grid(row=2, column=2, padx=1, pady=1)

label_quantidade = ctk.CTkLabel(janela, text="Quantidade:")
label_quantidade.grid(row=3, column=2, pady=15, padx=(10, 0), sticky="w")

quantidade = ctk.CTkEntry(janela, width=40)
quantidade.grid(row=3, column=2, padx=(0, 10), sticky="e")
    
btn_executar = ctk.CTkButton(janela, text="Executar", command=executar_tarefa, width=140)
btn_executar.grid(row=4, column=2, padx=1, pady=1)

janela.mainloop()