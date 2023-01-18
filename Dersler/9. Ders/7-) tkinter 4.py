from tkinter import *
import pyautogui

window = Tk()

window.title("Mouse hareket")

label = Label(window,text="merhaba")
label2 = Label(window,text="merhaba", font=("Arial Bold", 20))
label.grid(column=0, row=0)
label2.grid(column=0, row=1)

window.geometry('500x500')

buton = Button(window, text="Tıkla")
buton.grid(column=0, row=2)


def Tiklandi():
    pyautogui.moveTo(1000, 1000, duration=2,tween=pyautogui.easeInOutQuad)


btn2 = Button(window, text="Tıkla Renkli",bg="orange", fg="tomato",width=10, height=10,command=Tiklandi)

btn2.grid(column=0, row=3)

window.mainloop()
