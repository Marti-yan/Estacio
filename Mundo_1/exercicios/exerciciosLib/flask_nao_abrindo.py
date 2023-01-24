from flask import flask

app = Flask(__name__)
 
@app.route('/')
def ola_mundo():
    return "Olá, mundo."
 
if __name__ == '__main__':
    app.run()






