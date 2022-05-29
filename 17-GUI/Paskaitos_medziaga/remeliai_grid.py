from tkinter import *

langas = Tk()

uzrasas1 = Label(langas, text="Vardas")
laukas1 = Entry(langas)
uzrasas2 = Label(langas, text="Pavardė")
laukas2 = Entry(langas)
varnele = Checkbutton(langas, text="Pažymėk varnelę")

uzrasas1.grid(row=0, column=0, sticky=E)
laukas1.grid(row=0, column=1)
uzrasas2.grid(row=1, column=0, sticky=E)
laukas2.grid(row=1, column=1)
varnele.grid(row=2, columnspan=2)

langas.mainloop()
