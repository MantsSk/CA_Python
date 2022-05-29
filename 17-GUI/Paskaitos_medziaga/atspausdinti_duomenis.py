from tkinter import *

langas = Tk()

def spausdinti():
    ivesta = laukas1.get()
    rezultatas["text"] = ivesta

uzrasas1 = Label(langas, text="Įrašykite žodį")
laukas1 = Entry(langas)
mygtukas = Button(langas, text="Įvesti", command=spausdinti)
rezultatas = Label(langas, text="")

uzrasas1.grid(row=0, column=0)
laukas1.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
rezultatas.grid(row=1, columnspan=3)

langas.mainloop()
