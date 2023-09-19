import time
import subprocess

while True:
    # subprocess.run(['python', 'votacao-pyautogui.py'])
    subprocess.run(['python', 'votacao-selenium.py'])
    time.sleep(125)
