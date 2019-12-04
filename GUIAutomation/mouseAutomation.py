import pyautogui
# returns resolution of screen, width, height
print(pyautogui.size())

width, height = pyautogui.size()
print(width)

#coordinates of mouse cursor
print(pyautogui.position())

#reposition mouse cursor
pyautogui.moveTo(10,10)

#moves cursor speed based on duration seconds
pyautogui.moveTo(1000,400, duration=3.0)

#move relative to current position (also dragRel and dragTo)
pyautogui.moveRel(100,50, duration=3)

#has the mouse click on a position (also doubleclick, right click etc)
pyautogui.click(1278,66)


# drawing spiral
pyautogui.click() #click to bring program in focus
distance = 200
while distance>0:
    pyautogui.dragRel(distance, 0, duration=0.1 ) #move right
    distance = distance-25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0.1) # move down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.1) #move left
    distance = distance-25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=0.1) #move up

#shows mouse coordinates as you move around
#best to run from terminal also shows RGB 
pyautogui.displayMousePosition()