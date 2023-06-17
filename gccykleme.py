# -*- coding: utf-8 -*-
from tkinter import * 
import tkinter.messagebox as box
import os
window = Tk()
window.title("Pardus GCC İnstaller ")
lbl = Label(window, text=" GCC İNSTALLER", font=("Arial Bold", 30))
lbl.grid(column=3, row=3)
window.geometry("600x290")
def clicked():
    os.system("bash gccinstall.sh")
btn = Button(window, text="Buton'a Bas ", bg="black", fg="white", command=clicked)
btn.grid(column=6, row=6)
window.mainloop()