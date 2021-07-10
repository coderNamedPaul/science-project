import pyautogui as pg
from time import sleep

sleep(3)
for i in range(1000):
    pg.moveTo(17, 175)
    pg.leftClick()
    pg.moveTo(131, 980)
    pg.leftClick()
    sleep(4)
