import pyautogui
import keyboard
import time
import sys

# Segurança do PyAutoGUI (mover mouse pro canto superior esquerdo para parar)
pyautogui.FAILSAFE = True

print("Iniciando em 3 segundos...")
print("Pressione ESC para parar.")
time.sleep(3)

try:
    while True:
        # Se apertar ESC → para
        if keyboard.is_pressed("esc"):
            print("Programa encerrado pelo usuário.")
            break

        # Procura o botão na tela inteira
        botao = pyautogui.locateOnScreen("botao.png", confidence=0.8)

        if botao is not None:
            print("Botão encontrado! Clicando...")
            
            # Clica no centro
            pyautogui.click(pyautogui.center(botao))
            
            # Se quiser que clique só uma vez, descomenta a linha abaixo:
            # break

        time.sleep(0.3)  # evita usar 100% da CPU

except pyautogui.FailSafeException:
    print("FailSafe ativado! Mouse foi para o canto.")
    sys.exit()