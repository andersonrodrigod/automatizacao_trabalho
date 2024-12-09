import pyperclip
import pandas as pd
import os
import pyautogui as py
import time
import json


def cod():
    return pyperclip.paste()

def name():
    return pyperclip.paste()

def cod_proc():
    return pyperclip.paste()

def name_proc():
    return pyperclip.paste()

def info_assistent():
    return pyperclip.paste()

def info_medico():
    return pyperclip.paste()

def medico_requesting():
    return pyperclip.paste()

def copy_input():
    py.hotkey("ctrl", "a")
    time.sleep(0.5)
    py.hotkey("ctrl", "c")
    time.sleep(0.5)
    py.hotkey("ctrl", "tab")

time.sleep(3)

def save_data():
    copy_input()
    codigo = cod()
    copy_input()
    nome = name()
    copy_input()
    codigo_procedimento = cod_proc()
    copy_input()
    nome_procedimento = name_proc()
    copy_input()
    info_assistente = info_assistent()
    copy_input()
    infor_medico = info_medico()

    dados = {
        "codigo": codigo,
        "nome": nome,
        "codigo_procedimento": codigo_procedimento,
        "nome_procedimento": nome_procedimento,
        "info_assistente": info_assistente,
        "info_medico": infor_medico
    }

    return dados

dados = save_data()

if os.path.exists("dados_coletados.json"):
    with open("dados_coletados.json", "r") as f:
        dados_existentes = json.load(f)
else:
    dados_existentes = []

dados_existentes.append(dados)

with open("dados_coletados.json", "w", encoding="utf-8") as f:
    json.dump(dados_existentes, f, indent=4, ensure_ascii=False)

print(dados)






