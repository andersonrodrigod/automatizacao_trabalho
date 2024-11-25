import pyperclip
import pandas as pd
import os
import pyautogui as py
import time
# Avisar ao usuário para selecionar o texto e copiá-lo

os.system("notepad.exe")
time.sleep(1)
py.hotkey("ctrl", "a")
time.sleep(0.5)
py.hotkey("ctrl", "c")

# Capturar o texto da área de transferência
texto_copiado = pyperclip.paste()

# Verificar se algo foi copiado
if not texto_copiado.strip():
    print("Nenhum texto foi copiado. Tente novamente.")
else:
    print(f"Texto capturado: {texto_copiado}")

    # Salvar o texto em um arquivo Excel
    dados = {"Texto": [texto_copiado]}  # Organizar o texto em uma tabela
    df = pd.DataFrame(dados)

    # Salvar no arquivo Excel
    caminho_excel = "info.xlsx"
    df.to_excel(caminho_excel, index=False, sheet_name="Texto Copiado")

    print(f"Texto salvo com sucesso no arquivo: {caminho_excel}")