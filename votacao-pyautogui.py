#pip install pyperclip
#pip install pyautogui

import pyperclip
import pyautogui as pa
import time

pa.PAUSE = 1

# Passo 1: Entrar no sistema (no nosso caso, entrar no link)
pa.hotkey("alt", "tab")
time.sleep(1)

pa.hotkey("ctrl", "t")
time.sleep(1)

pyperclip.copy("https://www.monolitospost.com/2023/08/01/os-melhores-do-ano-2023-categoria-odontologia/")
pa.hotkey("ctrl", "v")
pa.press("enter")
time.sleep(4)

pa.hotkey("PgDn")
time.sleep(3)
#print(f'A posição do arquivo é: {pa.position()}')
pa.click(x=70, y=446)

time.sleep(1)
#print(f'A posição do arquivo é: {pa.position()}')
pa.click(x=330, y=488)
time.sleep(5)
pa.hotkey("ctrl", "w")
time.sleep(1)
pa.hotkey("alt", "tab")


