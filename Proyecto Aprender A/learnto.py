from flask import Flask, render_template, session, url_for, request
from werkzeug.security import generate_password_hash
from flask_mysqldb import MySQL

from config import config

learntoApp = Flask(__name__)
db = MySQL(learntoApp)

@learntoApp.route('/')
def index():
    return render_template('home.html')

@learntoApp.route('/loginRegister', methods=['GET', 'POST'])
def loginRegister():
    if request.method == 'POST':
        nameu = request.form['nameu']
        emailu = request.form['emailu']
        passwordu = request.form['passwordu']
        passwordencryption = generate_password_hash(passwordu)
        
        registerU = db.connection.cursor()
        registerU.execute("INSERT INTO usuario (nameu, emailu, passwordu), VALUES(%s, %s, %s)", (nameu, emailu, passwordu))
        db.connection.commit()
        return render_template('home.html')
    return render_template('loginRegister.html')

@learntoApp.route('/loginUser')
def loginUser():
    return render_template('loginUser.html')

@learntoApp.route('/user/<nombre>')
def user(nombre):
    data={
        'titulo':'Usuario',
        'nombre':nombre
    }
    return render_template('user.html', data=data)

if __name__=='__main__':
    learntoApp.run(debug=True, port=3300)