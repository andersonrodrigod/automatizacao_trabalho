import pyperclip
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
    py.press("tab")
    copy_tab()
    medico_solicitante = medico_requesting()
    copy_tab()
    copy_click(251, 278)
    info_assistente = info_assistent()
    copy_click(307,418)
    info_medic = info_medico()
    py.click(139,113)
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


if os.path.exists("dados_coletados.json"):
    with open("dados_coletados.json", "r", encoding="utf-8") as f:
        dados_existentes = json.load(f)
        max_id = 0
        if dados_existentes:
            for item in dados_existentes:
                if item["id"] > max_id:
                    max_id = item["id"]
else:
    dados_existentes = []
    max_id = 0

id_count = max_id + 1
for _ in range(36):
    time.sleep(1.5)
    dados = save_data()
    dados_coletados.append(dados)
    id_count += 1

dados_existentes.extend(dados_coletados)

with open("dados_coletados.json", "w", encoding="utf-8") as f:
    json.dump(dados_existentes, f, indent=4, ensure_ascii=False)

print(dados)






