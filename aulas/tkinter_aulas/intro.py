import tkinter as tk
from tkinter import ttk
# Botão (Button):
#     É usado para exibir os botões na aplicação. São usados, por exemplo, para confirmar uma ação de salvar os dados.
# Telas (Canvas):
#     É usado para desenhar formas, como linhas, ovais, polígonos e retângulos.
# Botão de verificação (Checkbutton):
#     É usado para exibir várias opções como caixas de seleção. O usuário pode selecionar várias opções ao mesmo tempo.    
# Entrada de texto (Entry):
#     É usado para exibir uma caixa de texto de linha única para que o usuário digite valores de entrada. 
# Quadros (Frame):	
#     É usado como um widget de contêiner, isso significa que outros componentes são adicionados a ele com o objetivo de organizar outros widgets.   
# Rótulo (Label):	
#     É usado para fornecer uma legenda de linha única para outros widgets. Também pode conter imagens.
# Caixa de listagem (Listbox):   	
#     É usado para fornecer uma lista de opções para um usuário.   
# Menubutton:	
#     É usado para exibir opções no menu.    
# Menu:	
#     É usado para fornecer várias possibilidades de comandos a um usuário.
#     Esses comandos estão contidos no Menubutton.    
# Mensagem (Message):	
#     É usado para exibir uma mensagem de texto e um botão para o usuário confirmar uma ação    
# Botão de rádio (Radiobutton):	
#     É usado para exibir várias opções, como botões de rádio. O usuário pode selecionar apenas uma opção por vez.    
# Escala (Scale):	
#     É usado para fornecer um widget de controle deslizante.    
# Barra de rolagem (Scrollbar):
#     É usado para adicionar capacidade de rolagem a vários widgets.   
# Texto (Text):	
#     É usado para exibir texto em várias linhas.    
# Toplevel:	
#     É usado para fornecer um contêiner de janela separado.    
# Spinbox:	
#     É uma variante do widget Entry padrão. Ele é usado para selecionar um número fixo de valores.    
# PanedWindow:	
#     É um widget de contêiner que pode conter qualquer número de painéis, organizados horizontalmente ou verticalmente.    
# LabelFrame:	
#     É um widget de contêiner simples. Seu objetivo principal é atuar como um espaçador, ou contêiner para layouts de janela.    
# tkMessageBox:	
#     Este módulo é usado para exibir caixas de mensagens.

#    1       2        3       4          5            6        7       8         9        10        11
# Window / Label / Button / Entry / Radiobutton / Checkbox / Text / Message / Sliders / Dialog / Combobox


# WINDOW
janela = tk.Tk()
janela.title("Titulo da janela")
janela.resizable(False,False)# impedi de redimendionar a janela    #True,True

# LABEL
lblRotulo = ttk.Label(janela, text="Componente Label" ).grid(column=0, row=0)

# BUTTON 
contador = 0
def contador_label(lblRotulo):
    def funcao_contar():
        global contador
        contador = contador + 1
        lblRotulo.config(text=str(contador))
        lblRotulo.after(1000, funcao_contar)
        funcao_contar()

lblRotulo = tk.Label(janela, fg="green" ).grid(column=1, row=1)
contador_label(lblRotulo) #era para aparecer a contagem, mas o exemplo veio com erro
btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy).grid(column=0, row=1)

# ENTRY
def mostrar_nomes():
   print("Nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))

tk.Label(janela,text="Nome").grid(row=3,column=0)
tk.Label(janela,text="Sobrenome").grid(row=4,column=0)
e1 = tk.Entry(janela)
e1.grid(row=3,column=1)
e2 = tk.Entry(janela)
e2.grid(row=4,column=1)

tk.Button(janela, text='Sair',command=janela.quit).grid(row=5,column=0,sticky=tk.W,pady=4)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=5,column=1,sticky=tk.W,pady=4)

# RADIOBUTTON
v = tk.IntVar()
tk.Label(janela,text="""Escolha uma linguagem de programação:""",justify = tk.LEFT, padx = 20).grid(row=6,column=0)
tk.Radiobutton(janela,text="python",padx = 25,variable=v,value=1).grid(row=7,column=0)
tk.Radiobutton(janela,text="C++",padx = 25,variable=v,value=2).grid(row=8,column=0)

# CHECKBOX
def escolha_carreira():
   print("Gerencial: %d,\nTécnica : %d" % (var1.get(), var2.get()))
   
ttk.Label(janela, text="Escolha sua vocação:").grid(row=9, sticky=tk.W)

var1 = tk.IntVar()
ttk.Checkbutton(janela, text="Gerencial", variable=var1).grid(row=10, sticky=tk.W)
var2 = tk.IntVar()
ttk.Checkbutton(janela, text="Técnica", variable=var2).grid(row=11, sticky=tk.W) 

ttk.Button(janela, text='Sair', command=janela.quit).grid(row=10,column=1, sticky=tk.W, pady=4)
ttk.Button(janela, text='Mostrar', command=escolha_carreira).grid(row=11, column=1, sticky=tk.W, pady=4)

# TEXT
T = tk.Text(janela, height=2, width=30)
T.grid(row=12)
T.insert(tk.END, "Este é um texto\ncom duas linhas\n")

# MESSAGE
mensagem_para_usuario = "Esta é uma mensagem.\n(Pode ser bastante útil para o usuário)"
msg = tk.Message(janela, text = mensagem_para_usuario)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.grid(row=13)

# SLIDER
def mostrar_valores():
   print (w1.get(), w2.get())

w1 = ttk.Scale(janela, from_=0, to=50)
w1.grid(row=14, columnspan=2)
w2 = ttk.Scale(janela, from_=0, to=100, orient=tk.HORIZONTAL)
w2.grid(row=15, columnspan=2)
ttk.Button(janela, text='Mostrar a Escala', command=mostrar_valores).grid(row=16, columnspan=2)

# DIALOG
from tkinter import messagebox as mb

def resposta():
   mb.showerror("Resposta", "Desculpe, nenhuma resposta disponível!")
def verificacao():
   if mb.askyesno('Verificar', 'Realmente quer sair?'):
      mb.showwarning('Yes', 'Ainda não foi implementado')
   else:
      mb.showinfo('No', 'A opção de Sair foi cancelada')

tk.Button(text='Sair', command=verificacao).grid(row=17, column=0)
tk.Button(text='Resposta', command=resposta).grid(row=17, column=1)

# COMBOBOX
ttk.Label(janela, text = "Combobox Widget",background = 'green', foreground ="white",font = ("Times New Roman", 15)).grid(row = 18, column = 1)
ttk.Label(janela, text = "Selecione um mês :",font = ("Times New Roman", 10)).grid(column = 0,row = 19, padx = 10, pady = 25)

n = tk.StringVar()
escolha = ttk.Combobox(janela, width = 27, textvariable = n)

escolha['values'] = (' Janeiro',' Fevereiro',' Março',' Abril',' Maio',' Junho',' Julho',' Agosto',' Setembro',' Outubro',' Novembro',' Dezembro')
escolha.grid(column = 1, row = 19)
escolha.current()


# Finalização
janela.mainloop()

