from tkinter import *
window = Tk()

window.title("Merhaba Python")

label = Label(window, text="Merhaba")
label2 = Label(window, text="Merhaba", font=("Arial Bold", 100))

label.grid(column=0, row=0)
label2.grid(column=5, row=0)
window.geometry('500x400')

window.mainloop()