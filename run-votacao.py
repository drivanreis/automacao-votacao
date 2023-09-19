import time
import subprocess


while True:
    try:
        subproc = subprocess.run(['python', 'votacao-selenium.py'])
        time.sleep(25)
    except Exception as e:
        subproc.terminate()
        print(f"Ocorreu um erro: {e}")
    finally:
        time.sleep(25)