from tkinter import *

langas = Tk()

kintamasis = StringVar()
# kintamasis = ""

def funkcija():
    kintamasis.set("Naujas tekstas")
    print(kintamasis.get())
