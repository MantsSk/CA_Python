from tkinter import *
langas = Tk()

def spausdinti(event):
    print("Paspaustas kairys pelės mygtukas!")

def spausdinti2(event):
    print("Paspaustas dešinys pelės mygtukas!")

def spausdinti3(event):
    print("Paspaustas ENTER!")

mygtukas = Button(langas, text="Spausdinti")
# https://web.archive.org/web/20190515021108id_/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html
mygtukas.bind("<Button-1>", spausdinti)
# O kaip atspausdinti be spausdinti2?
mygtukas.bind("<Button-3>", spausdinti2)
langas.bind("<Return>", spausdinti3)
mygtukas.pack()

langas.mainloop()
