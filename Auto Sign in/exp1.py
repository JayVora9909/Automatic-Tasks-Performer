import time

import pyautogui

if pyautogui.locateCenterOnScreen('Blank_Screen.png', confidence=0.9) is not None:
    time.sleep(2)
    print("seen")