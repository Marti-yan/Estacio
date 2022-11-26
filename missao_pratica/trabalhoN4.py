### Missão Prática N4 - Estácio ####
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Definiindo a classe Graficos
class Grafico:
    def __init__(self, lista_gastos):
        self.lista_gastos = lista_gastos
        self.facaGrafico()

    # Definindo os titulos do nosso grafico
    def padraoGrafico(self):
        plt.title('Gráficos de Despesas')
        plt.xlabel('Dia')
        plt.ylabel('Despesas em R$')

    # Colocando os dados no gráfico
    def facaGrafico(self):
        self.padraoGrafico()
        for gasto in self.lista_gastos:
            minhaLista = gasto.dicionario.items()
            cor = gasto.cor
            nome = gasto.nome
            x, y = zip(*minhaLista)
            plt.plot(x, y, label=nome, marker='o',
                     markerfacecolor='blue',
                     markersize=12,
                     color=cor,
                     linewidth=4)
        plt.legend()
        plt.show()

    # Função para tratar da regressão linear e aprendizagem
    def regressao_linear(self, id_grafico):
        gasto = self.lista_gastos[id_grafico]
        minhaLista = gasto.dicionario.items()
        cor = gasto.cor
        nome = gasto.nome
        alimentacao, valores = zip(*minhaLista)
        alimentacao = np.array(alimentacao)
        valores = np.array(valores)
        alimentacao = alimentacao.reshape(-1, 1)
        valores = valores.reshape(-1, 1)
        regr = LinearRegression()
        regr.fit(X=alimentacao, y=valores)
        plt.plot(alimentacao, regr.predict(alimentacao),
                 color='blue',
                 label='Regressão Linear')
        x, y = zip(*minhaLista)
        plt.plot(x, y, label = nome+str(" - original"),
                 marker='o',
                 markerfacecolor='olive',
                 markersize=12,
                 color=cor,
                 linewidth=4)
        plt.legend()
        plt.show()

# Classe que repesenta os dados
class Gastos:
    def __init__(self, dicionario, cor, nome):
        self.dicionario = dicionario
        self.cor = cor
        self.nome = nome

# Entrada de dados
# primeiro número representa o dia, segundo número representa a quantidade gasta R$
alimentacao = Gastos({1: 100, 2: 0, 3: 0, 4: 150, 5: 0}, 'lightblue', 'Alimentação')
vestuario = Gastos({1: 0, 2: 30, 3: 50, 4: 0, 5: 40}, 'red', 'Vestuário')
transporte = Gastos({1: 0, 2: 0, 3: 100, 4: 300, 5: 50}, 'olive', 'Transporte')
lista_gastos = [alimentacao,vestuario,transporte]

# Criacao do objeto grafico de Grafico
grafico = Grafico(lista_gastos)
id_mes = 0 # Representa alimentação
grafico.regressao_linear(id_mes)