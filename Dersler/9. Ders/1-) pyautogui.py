import pyautogui

pyautogui.FAILSAFE = False

pyautogui.moveTo(1, 1, duration=1,tween=pyautogui.easeOutElastic)
pyautogui.moveTo(30, 30, duration=5,tween=pyautogui.easeInOutQuad)
pyautogui.moveTo(100, 100, duration=2,tween=pyautogui.easeInCirc)
pyautogui.moveTo(20, 80, duration=2,tween=pyautogui.easeInBounce)
