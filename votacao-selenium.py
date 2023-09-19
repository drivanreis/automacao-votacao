#pip install selenium
#pip install pyautogui

import pyautogui as pa
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# Abre a URL desejada
url = "https://www.monolitospost.com/2023/08/01/os-melhores-do-ano-2023-categoria-odontologia/"
driver.get(url)

# Esperar a pagina carregar
time.sleep(3)

# Rolar a pagina para baixo
pa.hotkey("PgDn")
time.sleep(1)

try:
    # Encontra e clica no elemento HTML com XPath //*[@id="poll-answer-4332"]
    element1 = driver.find_element(By.XPATH, '//*[@id="poll-answer-4332"]')
    element1.click()
    
    # tempo para o usuario perceber o cliqui
    time.sleep(1)

    # Encontra e clica no elemento HTML com XPath //*[@id="polls-559-ans"]/p[1]/input
    element2 = driver.find_element(By.XPATH, '//*[@id="polls-559-ans"]/p[1]/input')
    element2.click()
    
    # tempo para o usuario perceber o cliqui
    time.sleep(1)

    # tempo para o usuario ver o resultado da votação
    time.sleep(5)

    # Rolar a pagina para baixo
    pa.hotkey("PgDn", "PgDn")
    time.sleep(2)

    # Encontra e clica no elemento HTML com XPath //*[@id="poll-answer-4332"]
    element1 = driver.find_element(By.XPATH, '//*[@id="poll-answer-3774"]')
    element1.click()
    
    # tempo para o usuario perceber o cliqui
    time.sleep(1)

    # Encontra e clica no elemento HTML com XPath //*[@id="polls-559-ans"]/p[1]/input
    element2 = driver.find_element(By.XPATH, '//*[@id="polls-561-ans"]/p[1]/input')
    element2.click()
    
    # tempo para o usuario perceber o cliqui
    time.sleep(1)

    # tempo para o usuario ver o resultado da votação
    time.sleep(5)

except Exception as e:
    # Se ocorrer um erro, imprima a mensagem de erro e encerre a página e o navegador
    print(f"Ocorreu um erro: {e}")

finally:
    # Fecha o navegador
    driver.quit()
