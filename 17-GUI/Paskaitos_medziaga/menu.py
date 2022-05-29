from tkinter import *
langas = Tk()

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
submeniu2 = Menu(meniu, tearoff = 0)
submeniu3 = Menu(meniu, tearoff = 0)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Pirmas")

submeniu.add_command(label="Antras")
submeniu.add_separator()
submeniu.add_command(label="Trečias")

meniu.add_cascade(label="Meniu 2",
menu=submeniu2)
submeniu2.add_command(label="1")
submeniu2.add_command(label="2")

meniu.add_cascade(label="Meniu 3",
menu=submeniu3)

langas.mainloop()
