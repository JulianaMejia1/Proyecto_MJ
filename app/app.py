from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)

# Lista para almacenar todas las transacciones
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    
