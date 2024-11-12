import pyautogui as py
import os
import time
import pyperclip
import keyboard


def exit_program():
    print("Encerrando Programa")
    os._exit(0)

largura, altura = py.size()

texto_copiado = r"C:\Users\ander\OneDrive\Área de Trabalho\Programação\projetos\editar_paint\imagens"

x = largura / 2
y = altura / 2

count = 1

for _ in range(1):
    time.sleep(2)
    py.hotkey("win", 'd')
    time.sleep(1)
    py.click(251, 1057)
    time.sleep(1)
    py.click(x, y, button="right")
    time.sleep(1)
    for _ in range(3):
        time.sleep(0.2)
        py.press("down")
    py.press("enter")
    time.sleep(0.2)
    py.click(473, 1059)
    time.sleep(1)
    py.click(x, y)
    py.hotkey("ctrl", "v")
    time.sleep(1)
    py.press("alt")
    time.sleep(1)
    py.press("f")
    time.sleep(1)
    py.press("a")
    time.sleep(1)
    py.press("j")
    time.sleep(1)
    py.click(160, 61)
    time.sleep(1)
    pyperclip.copy(texto_copiado)
    py.hotkey("ctrl", "v")
    py.press("enter")
    py.click(355, 396)
    count_str = str(count)
    py.write(count_str, interval=0.5)
    py.press("enter")
    time.sleep(1)
    py.hotkey("win", 'd')
    time.sleep(1)
    py.click(251, 1057)
    py.press("right")
    count += 1

