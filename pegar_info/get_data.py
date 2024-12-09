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

def medico_requesting():
    return pyperclip.paste()

def info_assistent():
    return pyperclip.paste()

def info_medico():
    return pyperclip.paste()



def copy_tab():
    time.sleep(0.5)
    py.hotkey("ctrl", "c")
    time.sleep(0.5)
    py.press("tab")

def copy_click(x, y):
    py.click(x, y)
    time.sleep(0.5)
    py.hotkey("ctrl", "c")

def save_data():
    copy_tab()
    codigo = cod()
    copy_tab()
    nome = name()
    for _ in range(3):
        time.sleep(0.2)
        py.press("tab")
    copy_tab()
    codigo_procedimento = cod_proc()
    copy_tab()
    nome_procedimento = name_proc()
    copy_click("click no medico solicitante")
    medico_solicitante = medico_requesting()
    copy_click("click na informação do solicitante")
    info_assistente = info_assistent()
    copy_click("click na informação medica")
    info_medic = info_medico()
    py.click("click na cordenada do codigo")
    py.press("down")

    dados = {
        "id": id_count,
        "codigo": codigo,
        "nome": nome,
        "codigo_procedimento": codigo_procedimento,
        "nome_procedimento": nome_procedimento,
        "info_assistente": info_assistente,
        "info_medico": info_medic,
        "medico_solicitante": medico_solicitante
    }

    return dados

dados_coletados = []
id_count = 1
for _ in range(3):
    dados = save_data()
    dados_coletados.append(dados)
    id_count += 1

if os.path.exists("dados_coletados.json"):
    with open("dados_coletados.json", "r") as f:
        dados_existentes = json.load(f)
else:
    dados_existentes = []

dados_existentes.extend(dados_coletados)

with open("dados_coletados.json", "w", encoding="utf-8") as f:
    json.dump(dados_existentes, f, indent=4, ensure_ascii=False)

print(dados)






