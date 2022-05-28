#import libreria Flask
from flask import Flask, render_template

app = Flask(__name__)

#ruta principal
@app.route('/')

def principal():
    return render_template('index.html')

#Main del programa
if __name__ == '__main__':
#debug = True, para reiniciar automaticamente el servidor
    app.run(debug=True)