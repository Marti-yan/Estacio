from tkinter import *
from tkinter.ttk import *

root = Tk()

class Application():
    def __int__(self):
        self.root = root
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.tittle("Reservar Ferramentas")
        self.root.configure(background='#1e3743')
        #self.root.attributes('-fullscreen', True)
        self.root.geometry("600x500")
        self.root.resizable(True,True)


Application()
