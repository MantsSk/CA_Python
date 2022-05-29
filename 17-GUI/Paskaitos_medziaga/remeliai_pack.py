from tkinter import *

langas = Tk()

virsutinis = Frame(langas)
apatinis = Frame(langas)
tuscias = Frame(langas)

mygtukas1 = Button(virsutinis, text="1 mygtukas")
mygtukas2 = Button(virsutinis, text="2 mygtukas")
mygtukas3 = Button(virsutinis, text="3 mygtukas")
mygtukas4 = Button(apatinis, text="4 mygtukas")
mygtukas5 = Button(tuscias, text="5 mygtukas")

virsutinis.pack()
tuscias.pack()
apatinis.pack(side=BOTTOM)
mygtukas1.pack(side=LEFT)
mygtukas2.pack(side=LEFT)
mygtukas3.pack(side=LEFT)
mygtukas4.pack(side=BOTTOM, fill=Y)
#mygtukas5.pack()

langas.mainloop()
