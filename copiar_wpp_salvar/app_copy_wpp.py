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




largura, altura = py.size()

diretorio_salvar = ""

x = largura / 2
y = altura / 2

def corrigir_caminho(caminho):
    return os.path.normpath(caminho)


def copiar_wpp():
    py.click(x, y, button="right")
    for _ in range(3):
        py.press("down")
    time.sleep(1)
    py.press("enter")
    time.sleep(0.2)

def salvar_paint(count):
    if not diretorio_salvar:
        print("Erro: Diretório de salvamento não foi definido.")
        return
    
    py.hotkey("win", "d")
    time.sleep(1)
    os.system("start mspaint")
    time.sleep(0.5)
    py.click(x, y)
    time.sleep(0.5)
    py.hotkey("ctrl", "v")
    time.sleep(0.5)
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
    time.sleep(1)
    py.hotkey("ctrl", "v")
    time.sleep(1)
    py.press("enter")
    time.sleep(1)
    py.hotkey("ctrl", "l")
    py.press("enter")
    py.hotkey("shift", "tab")
    time.sleep(1)
    py.hotkey("shift", "tab")
    time.sleep(1)
    py.click(355, 396)
    count_str = str(count)
    py.write(count_str, interval=0.5)
    py.press("enter")
    time.sleep(0.5)
    py.hotkey("alt", "f4")

def proxima_imagem():
    py.hotkey("alt", 'tab')
    time.sleep(1)
    py.press("right")

def minimizar():
    # Minimiza a janela
    janela.iconify()
    
    
def salvando_imgs_wpp():
    count = 1
    try:
        quantidade_valor = int(quantidade.get())
        if quantidade_valor <= 0:
            raise ValueError("A quantidade deve ser maior que zero")


        time.sleep(3)
        for _ in range(quantidade_valor):
            copiar_wpp()
            salvar_paint(count)
            proxima_imagem()
            count += 1
        print("processo concluído")
    except ValueError:
        print("Por favor, insira um número válido na quantidade.")

def executar_tarefa():
    global quantidade

    if not diretorio_salvar:
        messagebox.showerror("Erro", "Por favor, selecione um diretório para salvar os arquivos.")
        return
    
    try:
        quantidade_valor = int(quantidade.get().strip())

        if quantidade_valor <= 0:
            messagebox.showerror("Erro", "A quantidade deve ser um número positivo.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para a quantidade.")
        return

    minimizar()
    salvando_imgs_wpp()
    

def escolher_diretorio():
    global diretorio_salvar
    diretorio_salvar = fd.askdirectory()
    if diretorio_salvar:
        diretorio_salvar = corrigir_caminho(diretorio_salvar)
        label_diretorio.configure(text=f"Diretório: {diretorio_salvar}")

def somente_numeros(text):
    return text.isdigit()

label_diretorio = ctk.CTkLabel(janela, text="Diretório: Não definido", wraplength=650)
label_diretorio.pack(pady=10)

btn_escolher_diretorio = ctk.CTkButton(janela, text="Escolher Diretório", command=escolher_diretorio)
btn_escolher_diretorio.pack(pady=10)

label_quantidade = ctk.CTkLabel(janela, text="Quantidade")
label_quantidade.pack()
quantidade = ctk.CTkEntry(janela, width=40)
quantidade.pack(pady=10)
    

btn_executar = ctk.CTkButton(janela, text="Executar", command=executar_tarefa)
btn_executar.pack(pady=20)




janela.mainloop()