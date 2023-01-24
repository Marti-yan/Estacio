import tkinter
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import messagebox

def acao():
    print("butão presionado")
    msg = messagebox.showinfo("Alerta!!!", texto.get())
    
    
principal = tkinter.Tk()
btn = Button(principal, text="Olá", command=acao).grid(row=0, column=2)

texto = Entry(principal).grid(row=0, column=1)

etiqueta = Label(principal, text="Label").grid(row=0, column=0)
principal.mainloop()