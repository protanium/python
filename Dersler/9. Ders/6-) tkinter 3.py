from tkinter import *

window = Tk()
window.title("Giris")

label = Label(window,text="merhaba")
label2 = Label(window,text="merhaba",font=("Arial Bold", 45))
label.grid(column=0, row=0)
label2.grid(column=1, row=0)

window.geometry('400x400')

def Tiklandi2():
    label2.configure(text="aaaaaa")

buton = Button(window,text="tıkla",command=Tiklandi2)


buton.grid(column=1, row=1)

def Tiklandi():
    label.configure(text="Butona tıklandı")




buton2 = Button(window, text="Tıkla Renkli",bg="orange", fg="red",width=10, height=10,command=Tiklandi)

buton2.grid(column=1, row=3)

window.mainloop()
