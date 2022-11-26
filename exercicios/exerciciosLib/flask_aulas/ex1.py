from flask import Flask
app = Flask(__name__)

@app.route('/')
def cumprimento():
    boas_vindas = '<h1> Olá, programadores! </h1>'
    link = '<p> <a href="user/Usuario"> clique aqui'
    return boas_vindas + link

@app.route('/user')
@app.route('/user/<nome>')
def user(nome= "Usuário"):
    personalizar = f'<h1> Olá, {nome}! </h1>'
    instrucao = '<p> Altere o nome <em> endereço do browser</em> e recarregue a pagina.</p>'
    return personalizar + instrucao


app.run()