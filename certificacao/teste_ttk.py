"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

vlist = ["Option1", "Option2", "Option3",
         "Option4", "Option5"]

Combo = ttk.Combobox(frame, values=vlist)
Combo.set("Pick an Option")
Combo.pack(padx=5, pady=5)

root.mainloop()

from tkinter import *
janela = Tk()

barra = Scrollbar(janela)
canvas = Canvas(janela, yscrollcommand=barra.set)
barra.config(command=canvas.yview)
barra.pack(side='right', fill='y')

frame = Frame(canvas)
canvas.pack(side='top', fill='both', expand=True)
canvas.create_window(0, 0, window=frame)
for item in range(100):
    texto = Label(frame, text=f'barra de rolagem {item}')

janela.update()
canvas.config(scrollregion = canvas.bbox('all'))
janela.mainloop()

from tkinter import *
from tkinter.ttk import *

master = Tk()
master.geometry("200x200")


def openNewWindow():
    newWindow = Toplevel(master)

    newWindow.title("New Window")

    newWindow.geometry("200x200")

    Label(newWindow,
          text="This is a new window").pack()


label = Label(master,
              text="This is the main window")

label.pack(pady=10)
btn = Button(master,
             text="Click to open a new window",
             command=openNewWindow)
btn.pack(pady=10)
mainloop()]
"""
from tkinter import ttk
from tkinter import *

class Application():
    def __int__(self):
        self.root = Tk()
        self.tela()
        self.root.mainloop()
    def tela(self):
        self.root.title("Reservar Ferramentas")
        self.root.configure(background='#1e3743')
        self.root.geometry("600x500")
        self.root.resizable(True,True)

Application()
