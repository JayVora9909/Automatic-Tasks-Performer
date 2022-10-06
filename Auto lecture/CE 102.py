import pyautogui
import time
from playsound import playsound
from datetime import datetime as date

def Start_MS_Teams_Ideally() :
 pyautogui.click(1917, 1050) #clicks left bottom button to come at desktop
 x_MS_Teams_logo , y_MS_Teams_logo = pyautogui.locateCenterOnScreen('MS_Teams_logo.jpg', confidence=0.9)
 pyautogui.doubleClick(175, 216)
 time.sleep(15)
 pyautogui.click(50, 318)
 pyautogui.click(50, 318)

'''if (date.today().strftime("%A")=="Thursday") or (date.today().strftime("%A")=="Monday") :
 print("Yes")'''
time.sleep(3)
Start_MS_Teams_Ideally()

 
pyautogui.moveTo(500,618)
time.sleep(0.5)
pyautogui.scroll(-70)
time.sleep(0.5)
pyautogui.click(1587, 422)
time.sleep(2)

while pyautogui.locateCenterOnScreen('Join.png', confidence=0.9) ==None :
 playsound('E:\Jay\Python\Meeting not started.mp3')
 time.sleep(50)

 x_Join,y_Join = pyautogui.locateCenterOnScreen('Join.png', confidence=0.9)
 pyautogui.click(x_Join, y_Join)

while True :
 if pyautogui.locateCenterOnScreen('Unmuted.png', confidence=0.9) !=None :
  x_Unmuted, y_Unmuted =pyautogui.locateCenterOnScreen('Unmuted.png', confidence=0.9)
  pyautogui.click(x_Unmuted, y_Unmuted)
  pyautogui.moveTo(x_Unmuted-100,y_Unmuted+100)

