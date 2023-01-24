from flask import Flask
app = Flask(__name__)

@app.route('/')
def cumprimento():
    boas_vindas = '<h1> Olá, programadores! </h1>'
    link = '<p> Entre com 2 numeros </p>'
    return boas_vindas + link

@app.route('/somar/')
@app.route('/somar/<num01>/<num02>')
def soma(num01=0, num02=0):
    resultado = float(num01) + float(num02)
    return str(resultado)

app.run()
