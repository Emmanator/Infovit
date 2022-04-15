import tkinter

# Oppgave 1
gui = tkinter.Tk()

ramme = tkinter.Frame(gui)
ramme.pack()
knapp = tkinter.Button(ramme, text='Goodbye.', command=lambda: gui.destroy())
knapp.pack()
gui.mainloop()

# Oppgave 2
gui2 = tkinter.Tk()

teller = tkinter.IntVar()
teller.set(0)


# Funksjon for å trykke på knappen
def trykk(var, value):
    var.set(var.get() + value)


ramme2 = tkinter.Frame(gui2)
ramme2.pack()
knapp2 = tkinter.Button(ramme2, textvariable=teller, command=lambda: trykk(teller, 1))
knapp2.pack()
gui2.mainloop()
