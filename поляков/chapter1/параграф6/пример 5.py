import pyautogui as pg  # перед использованием скачать pyautogui
import os
from time import sleep
open('hello user.txt', 'w+')
os.startfile('hello user.txt')
sleep(1)
pg.write('hello, world!', 0.2)
