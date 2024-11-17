import customtkinter as ctk
import pyautogui as py
import time
import pyperclip

janela = ctk.CTk()
janela.title("SALVAR IMAGEM DO WHATS APP")
janela.geometry("700x400")
janela.minsize(width=700, height=350)
janela.maxsize(width=700, height=350)
janela.resizable(width=False, height=False)

largura, altura = py.size()

texto_copiado = r"C:\Users\ander\OneDrive\Área de Trabalho\Programação\projetos\copiar_wpp_salvar\imagens"

x = largura / 2
y = altura / 2




def copiar_wpp():
    py.click(x, y, button="right")
    for _ in range(3):
        py.press("down")
    time.sleep(1)
    py.press("enter")
    time.sleep(0.2)

def salvar_paint(count):
    py.click(473, 1059)
    time.sleep(0.5)
    py.click(x, y)
    py.hotkey("ctrl", "v")
    time.sleep(0.5)
    py.press("alt")
    time.sleep(0.5)
    py.press("f")
    time.sleep(0.5)
    py.press("a")
    time.sleep(0.5)
    py.press("j")
    time.sleep(0.5)
    py.click(160, 61)
    time.sleep(0.5)
    pyperclip.copy(texto_copiado)
    py.hotkey("ctrl", "v")
    py.press("enter")
    py.click(355, 396)
    count_str = str(count)
    py.write(count_str, interval=0.5)
    py.press("enter")
    time.sleep(1)

def proxima_imagem():
    py.hotkey("win", 'd')
    time.sleep(1)
    py.click(251, 1057)
    py.press("right")

def minimizar():
    # Minimiza a janela
    janela.iconify()
    
    
def salvando_imgs_wpp():
    count = 1
    time.sleep(3)
    for _ in range(5):
        copiar_wpp()
        salvar_paint(count)
        proxima_imagem()
        count += 1

def executar_tarefa():
    minimizar()
    salvando_imgs_wpp()
    
    
    

    

    
    
btn_executar = ctk.CTkButton(janela, text="Executar", command=executar_tarefa)
btn_executar.pack(pady=110)













janela.mainloop()