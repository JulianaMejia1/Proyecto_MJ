from flask import Flask,request, render_template, redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key ='1036252265'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''     
app.config['MYSQL_DB']='code_makers_db'
mysql = MySQL(app)

@app.route('/')
def url():
    return redirect(url_for('index'))

@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

# FORMULARIO PARA LAS RESEÑAS
@app.route('/reseña', methods=['POST', 'GET'])
def reseña():
    if request.method == 'POST':
        res_nombre = request.form['res_nombre']
        res_mejor = request.form['res_mejor']
        res_utilidad = request.form['res_utilidad']
        print(res_nombre,res_mejor,res_utilidad)
        cur = mysql.connection.cursor()     
        cur.execute('INSERT INTO resena (res_nombre,res_mejor,res_utilidad) VALUES (%s, %s, %s)',
        (res_nombre,res_mejor,res_utilidad))
        mysql.connection.commit()
        return redirect(url_for('index'))
    return render_template('reseña.html')

# Ruta para redirigir a WhatsApp
@app.route('/whatsapp')
def whatsapp():
    whatsapp_url = "https://api.whatsapp.com/send?phone=573506206995&text=Hola"
    return redirect(whatsapp_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    
