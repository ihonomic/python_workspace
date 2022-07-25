#! python3
from time import time, sleep
import pyautogui

# pip install pyautogui - virtual keypresses and mouse clicks
#   WARNING - logout from automation ctrl-alt-del

sleep(5)
pyautogui.PAUSE = 1.5  # Pause after each action
pyautogui.FAILSAFE = True   #

print(pyautogui.size())

# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)
# .moveRel() - Relative to the mouse current location
#   .position() - Mouse current location
#   .click(100, 150, button='left') , doubleClick(), rightClick(), middleClick()
#   .screenshot()

while True:
    pyautogui.scroll(200)
