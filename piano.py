from pyautogui import *
import pyautogui
from pyautogui import pixel
import time
import keyboard
import random
import win32api, win32con

route = './screenshots/score' + str(random.uniform(1, 10)) + '.png'

def click(x,y, option):
    win32api.SetCursorPos((x,y))

    if(option == "restart"):
        pyautogui.screenshot(route, region=(1357,304, 543, 58))

        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        return 0

    keyboard.press('space')

while keyboard.is_pressed('q') == False:
    try:
        # big cactus
        if pyautogui.pixel(580, 579)[0] == 172:
            click(450, 579, "a")
        # regular
        if pyautogui.pixel(450, 680)[0] == 172:
            click(450, 680, "a")
        # small cactus
        if pyautogui.pixel(450, 690)[0] == 172:
            click(450, 690, "a")
        # restart button
        elif pyautogui.pixel(960, 531)[0] == 172:
            click(666, 500, "restart")
    except:
        print('cant see pixel ' + str(datetime.datetime.now()))

# display mouse positio (x / y / rgb)
# pyautogui.displayMousePosition()