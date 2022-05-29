from tkinter import *

langas = Tk()
sarasas = range(1, 200)

def spausdinti():
    pasirinkta = sarasas[boksas.curselection()[0]]
    uzrasas["text"] = pasirinkta

mygtukas = Button(langas, text="Spausdinti",
command=spausdinti)

uzrasas = Label(langas, text="Nieko")
boksas = Listbox(langas, selectmode=SINGLE)
boksas.insert(END, *sarasas)
boksas.pack(side=LEFT)
mygtukas.pack()
uzrasas.pack()
langas.mainloop()
