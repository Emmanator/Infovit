import tkinter


# Oppgave 1
def oppg1():
    gui = tkinter.Tk()

    ramme = tkinter.Frame(gui)
    ramme.pack()
    knapp = tkinter.Button(ramme, text='Goodbye.', command=lambda: gui.destroy())
    knapp.pack()
    gui.mainloop()


# Oppgave 2
def oppg2():
    gui = tkinter.Tk()

    teller = tkinter.IntVar()
    teller.set(1)

    # Funksjon for å trykke på knappen
    def trykk(var, value):
        var.set(var.get() * value)

    ramme = tkinter.Frame(gui)
    ramme.pack()
    knapp = tkinter.Button(ramme, textvariable=teller, command=lambda: trykk(teller, 2))
    knapp.pack()
    gui.mainloop()

oppg1()
oppg2()

