#pip install selenium

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

try:
    # Encontra e clica no elemento HTML com XPath //*[@id="poll-answer-4332"]
    element1 = driver.find_element(By.XPATH, '//*[@id="poll-answer-4332"]')
    element1.click()

    # tempo para o usuario perceber o cliqui
    time.sleep(2)

    # Encontra e clica no elemento HTML com XPath //*[@id="polls-559-ans"]/p[1]/input
    element2 = driver.find_element(By.XPATH, '//*[@id="polls-559-ans"]/p[1]/input')
    element2.click()

    # Simula pressionar a tecla
    element2.send_keys(Keys.ARROW_DOWN)

    
    # tempo para o usuario perceber o cliqui
    time.sleep(2)

    # tempo para o usuario ver o resultado da votação
    time.sleep(5)

    # Encontra e clica no elemento HTML com XPath //*[@id="poll-answer-4332"]
    element3 = driver.find_element(By.XPATH, '//*[@id="poll-answer-3774"]')
    element3.click()

    # tempo para o usuario perceber o cliqui
    time.sleep(2)

    # Encontra e clica no elemento HTML com XPath //*[@id="polls-559-ans"]/p[1]/input
    element4 = driver.find_element(By.XPATH, '//*[@id="polls-561-ans"]/p[1]/input')
    element4.click()

    # Simula pressionar a tecla
    element4.send_keys(Keys.ARROW_DOWN)

    # tempo para o usuario perceber o cliqui
    time.sleep(2)

    # tempo para o usuario ver o resultado da votação
    time.sleep(5)

except Exception as e:
    # Se ocorrer um erro, imprima a mensagem de erro e encerre a página e o navegador
    print(f"Ocorreu um erro: {e}")

finally:
    # Fecha o navegador
    driver.quit()
