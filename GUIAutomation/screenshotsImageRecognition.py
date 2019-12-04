import pyautogui
import os

os.chdir('D:\Dropbox\CodingResources\webDevelopmentProjects\Mine\practice-python-exercises\GUIAutomation')


#take screenshot and save to file
pyautogui.screenshot('example2.png')

#locate image on screen from screenshot
print(pyautogui.locateOnScreen('seven.png'))

#locate center of image on screen from screenshot
print(pyautogui.locateCenterOnScreen('seven.png'))

#move to center of image on screen
pyautogui.moveTo(1032, 644, duration=1)
pyautogui.click()