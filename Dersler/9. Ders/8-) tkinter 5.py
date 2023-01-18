from tkinter import *
import pyautogui

window = Tk()


label = Label(window, text="Merhaba")
label2 = Label(window, text="Merhaba", font=("Arial Bold", 50))
label.grid(column=0, row=0)
label2.grid(column=0, row=1)

window.geometry('500x500')
text2 = Entry(window, width=10, font=("Courier New", 20))
text2.grid(column=0, row=3)

def Tiklandi2():
    text2.insert(INSERT,"aaa")
buton = Button(window, text="Tıkla",command=Tiklandi2)
buton.grid(column=1, row=1)

def Tiklandi():
    pyautogui.moveTo(100, 100, duration=1,tween=pyautogui.easeInOutQuad)


buton2 = Button(window, text="Tıkla Renkli",bg="orange", fg="red",width=10, height=10,command=Tiklandi)

buton2.grid(column=1, row=3)

text = Entry(window, width=10)
text.grid(column=0, row=2)


window.mainloop()
