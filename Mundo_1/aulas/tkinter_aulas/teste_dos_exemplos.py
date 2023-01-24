# import tkinter as tk
# janela = tk.Tk()
# T = tk.Text(janela, height=2, width=30)
# T.pack()
# T.insert(tk.END, "Este é um texto\ncom duas linhas\n")
# tk.mainloop()

import tkinter as tk
from tkinter import ttk
# Criação de uma janela tkinter
janela = tk.Tk()
janela.title('Combobox')
janela.geometry('500x250')
# Componente Label
ttk.Label(janela, text = "Combobox Widget",background = 'green', foreground ="white",font = ("Times New Roman", 15)).grid(row = 0, column = 1)
# Componente Label
ttk.Label(janela, text = "Selecione um mês :",font = ("Times New Roman", 10)).grid(column = 0,row = 5, padx = 10, pady = 25)
# Componente Combobox
n = tk.StringVar()
escolha = ttk.Combobox(janela, width = 27, textvariable = n)
# Adição de itens no Combobox
escolha['values'] = (' Janeiro',' Fevereiro',' Março',' Abril',' Maio',' Junho',' Julho',' Agosto',' Setembro',' Outubro',' Novembro',' Dezembro')
escolha.grid(column = 1, row = 5)
escolha.current()
janela.mainloop()
