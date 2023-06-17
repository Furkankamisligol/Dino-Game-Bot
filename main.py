import time
import pyautogui
from PIL import ImageGrab


def detect_collision():
    for x in range(665, 675):
        for y in range(332, 335):
            pixel = data[x, y]
            if pixel[0] < 100 and pixel[1] < 100 and pixel[2] < 100:
                return True
    return False


def detect_obstacle():
    for x in range(280, 330):
        for y in range(420, 480):
            pixel = data[x, y]
            if pixel[0] < 100 and pixel[1] < 100 and pixel[2] < 100:
                return True
    return False


def jump():
    pyautogui.press('up')
    time.sleep(0.07)
    pyautogui.press('down')


def restart_game():
    pyautogui.press('space')


time.sleep(5)

while True:
    image = ImageGrab.grab()
    data = image.load()

    if detect_collision():
        restart_game()
    elif detect_obstacle():
        jump()

    time.sleep(0.05)
