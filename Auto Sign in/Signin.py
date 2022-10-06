import pyautogui
# from PIL import Image, ImageGrab
import time

'''def Not_Blank_Screen(data):
    for i in range(30, 1890):
        for j in range(40, 1000):
            if data[i, j] < 240:
                return True
    else:
        return False
'''

i = 0
not_done = True
while not_done:
    time.sleep(0.5)
    if pyautogui.locateCenterOnScreen('Username.png', confidence=0.9) is not None:
        time.sleep(.1)
        if pyautogui.locateCenterOnScreen('Username.png', confidence=0.9) is not None:
            x, y = pyautogui.locateCenterOnScreen('Username.png', confidence=0.9)
            pyautogui.click(x, y)
            pyautogui.typewrite('user id')
            time.sleep(.1)
    if pyautogui.locateCenterOnScreen('Password.png', confidence=0.9) is not None:
        time.sleep(.1)
        if pyautogui.locateCenterOnScreen('Password.png', confidence=0.9) is not None:
            x, y = pyautogui.locateCenterOnScreen('Password.png', confidence=0.9)
            pyautogui.click(x, y)
            pyautogui.typewrite('Password')
            time.sleep(.1)
    if pyautogui.locateCenterOnScreen('Signin.png', confidence=0.9) is not None:
        time.sleep(.1)
        if pyautogui.locateCenterOnScreen('Signin.png', confidence=0.9) is not None:
            x, y = pyautogui.locateCenterOnScreen('Signin.png', confidence=0.9)
            pyautogui.click(x, y)
    '''image = ImageGrab.grab().convert('L')
    data = image.load()'''
    time.sleep(0.1)
    if pyautogui.locateCenterOnScreen('Homepage.png', confidence=0.9) is not None:
        not_done = False
    else:
        if pyautogui.locateCenterOnScreen('Redo.png', confidence=0.9) is not None:
            x, y = pyautogui.locateCenterOnScreen('Redo.png', confidence=0.9)
            pyautogui.click(x, y)
    i = (i + 1) % 3
    if i == 0:
        time.sleep(7)
