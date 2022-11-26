from tkinter import *

def funcClick():
    frase2 = Label(janela, text="botão foi pressionado").pack()
    # print("botão foi pressionado")
    
janela = Tk()

frase =Label(janela, text="para observar o clique do bortão, clique novamente").pack()
button = Button(janela, text="Click here", command = funcClick).pack()

janela.mainloop()