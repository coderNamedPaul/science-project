import pyautogui as pg
from time import sleep

sleep(3)
for i in range(50):
    pg.moveTo(17, 152)
    pg.leftClick()
    pg.moveTo(131, 974)
    pg.leftClick()
    sleep(4)
