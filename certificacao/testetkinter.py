"""
import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''
    #print(texto)
    texto_cotacoes["text"] = texto

#pegar_cotacoes()


janela = Tk()
janela.title("Cotação Atual das Moedas")


texto_inicial = Label(janela,text= "Clique no botão para ver as cotações das moedas")
texto_inicial.grid(column=0, row=0, padx=15, pady=10)

button = Button(janela,text= "Buscar cotação", command=pegar_cotacoes)
button.grid(column=0, row=1, padx=15, pady=10)

texto_cotacoes = Label(janela, text="USD: \n EUR: \n BTC: ")
texto_cotacoes.grid(column=0, row=2, padx=15, pady=10)

janela.mainloop()

"""

from tkinter import *

root = Tk()

frame = Frame(root, width=300, height=300)
frame.pack(expand=True, fill=BOTH)

canvas = Canvas(frame, bg='white', width=300, height=300,
                scrollregion=(0, 0, 500, 500))



vbar = Scrollbar(frame, orient=VERTICAL)
vbar.pack(side=RIGHT, fill=Y)
vbar.config(command=canvas.yview)

#canvas.config(width=300, height=300)
canvas.config( yscrollcommand=vbar.set)
canvas.pack(side=LEFT, expand=True, fill=BOTH)

root.mainloop()














