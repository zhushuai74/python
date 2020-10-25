import pyautogui
x,y = pyautogui.position()
# pyautogui.click(1523,42)
# pyautogui.moveTo(x,y)
im = pyautogui.screenshot()
print(im.getpixel((x,y)))