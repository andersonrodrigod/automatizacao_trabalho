import pyautogui
import time
import keyboard  # Biblioteca para capturar a tecla de saída

# Função para movimentar o mouse e clicar
def automacao_mouse():
    # Mover o mouse para uma posição (x=500, y=500)
    pyautogui.moveTo(500, 500, duration=1)
    # Clicar na posição atual do mouse
    pyautogui.click()

# Loop principal
try:
    while True:
        # Verifica se a tecla 'esc' foi pressionada para encerrar o código
        if keyboard.is_pressed('esc'):
            print("Programa encerrado.")
            break
        
        # Executa a automação de mouse
        automacao_mouse()
        
        # Aguarda 2 segundos antes de realizar a próxima automação
        time.sleep(2)
        
except KeyboardInterrupt:
    print("Programa interrompido manualmente.")
