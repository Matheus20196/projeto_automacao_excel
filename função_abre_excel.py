import pyautogui as pg 
import clipboard as cp
import time

def abre_excel():
    time.sleep(1)
    pg.press('Win')
    time.sleep(1)
    cp.copy('Excel')
    time.sleep(1)
    pg.write(cp.paste())
    time.sleep(1)
    pg.press('Enter')


