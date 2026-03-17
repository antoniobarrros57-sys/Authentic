from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time

driver = webdriver.Firefox()
driver.get("https://www.typing.com/")

def juntar():
    letras = driver.find_elements(By.CLASS_NAME, "screenIntro-letter")

    palavra = ""

    for letra in letras:
        palavra += letra.text
    time.sleep(1)
    keyboard.write(palavra, delay=0.2)

print("deseja executar-lo agora?")
time.sleep(1)
while True:
    resposta = input("[y/n] ")
    if resposta == "y":
        juntar()
        break
    elif resposta == "n":
        print("programa encerrado")                       
        break
        
    else:
        print("valor invalido")