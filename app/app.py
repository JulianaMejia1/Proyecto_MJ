from flask import Flask, render_template, redirect
app = Flask(__name__)

# Lista para almacenar todas las transacciones
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

# Ruta para redirigir a WhatsApp
@app.route('/whatsapp')
def whatsapp():
    whatsapp_url = "https://api.whatsapp.com/send?phone=573506206995&text=Hola"
    return redirect(whatsapp_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    
