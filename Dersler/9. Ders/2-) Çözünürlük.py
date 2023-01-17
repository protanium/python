import pyautogui
import time

genislik, yukseklik = pyautogui.size()
print("Ekran çözünürlüğü:", genislik, yukseklik)

while True:
    mousex,mousey = pyautogui.position()
    print(mousex,mousey)


    time.sleep(0.7)