import pyautogui
#click then type string, interval is time in between keystrokes
pyautogui.click(); pyautogui.typewrite('Hello World', interval=0.3)

#give it multiple key presses
pyautogui.click(); pyautogui.typewrite(['a','b','left','left','X', 'Y'], interval=0.3)

#gives list of keyboard keys
print(pyautogui.KEYBOARD_KEYS)

#press single key
pyautogui.press('key')

#press shortcut keys in combination
pyautogui.hotkey('ctrl', 'o')