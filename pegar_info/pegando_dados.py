import pyperclip
import pandas as pd
import os
import pyautogui as py
import time




def copy_data():
    py.hotkey("ctrl", "a")
    time.sleep(1)
    py.hotkey("ctrl", "c")
    time.sleep(1)
    copied_date = pyperclip.paste()
    
    return copied_date


def flap_change(flap):
    py.hotkey("ctrl", str(flap))
    time.sleep(1)



def save_create(collected_data):

    file_path = "info.xlsx"

    data = collected_data
    
    collumns= ["Codigo da Carteirinha", "Nome", "Codigo do Procedimento", "Nome do Procedimento", "Informacao do Usuario", "Informacao Medica", "Telefone" ]

    while len(data) < len(collumns):
        data.append(None)

    df = pd.DataFrame([data], columns=collumns)

    if os.path.exists(file_path):
        
        existing_df = pd.read_excel(file_path)

        update_df = pd.concat([existing_df, df], ignore_index=True)

        update_df.to_excel(file_path, index=False)

        print("Arquivo subscrito com sucesso")
    else:

        df.to_excel(file_path, index=False)
        print("arquivo criado com sucesso")

num_users = 3 

for user in range(num_users):
    os.system("notepad.exe")
    time.sleep(3)

    initial_flap = 1
    collected_data = []

    for i in range(6):
        flap_change(initial_flap)
        data = copy_data()
        collected_data.append(data)
        initial_flap += 1

    py.hotkey("alt", "f4")

    save_create(collected_data)

    print(collected_data)