from multiprocessing import connection
import smtplib
from email.message import EmailMessage 
import re
from flask import Flask, render_template, session, url_for, request, redirect, jsonify, flash
from werkzeug.security import generate_password_hash
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_mysqldb import MySQL
import datetime
from config import config
import os
# Models:
from models.modelUser import ModelUser

# Entities:
from models.entities.User import User

learntoApp = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(learntoApp)
login_manager_app = LoginManager(learntoApp)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@learntoApp.before_request
def before_request():
    print("Antes de la petición...")


@learntoApp.after_request
def after_request(response):
    print("Después de la petición")
    return response

@learntoApp.route('/')
def index():
    return render_template('home.html')

    # ==============================
    # Rutas administrador y modales
    # ==============================
@learntoApp.route('/admin', methods = ['GET', 'POST'])
def admin():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    return render_template('admin.html', user = data)
    
    # Agregar - Ruta del botón --------->
@learntoApp.route('/add/', methods=['GET', 'POST'])
def admin_add():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        fullname = request.form['fullname']
        age = request.form['age']
        schoolgrade = request.form['schoolgrade']
        hash = generate_password_hash(password) 

        regUser = db.connection.cursor()
        query = "INSERT INTO user (username, email, password, fullname, age, schoolgrade) VALUES (%s, %s, %s, %s, %s, %s)"
        regUser.execute(query, (username, email, hash, fullname, age, schoolgrade))
        db.connection.commit()
        user = User(None, username, email, password, fullname, age, schoolgrade, None)
        logged_user = ModelUser.login(db, user)
        login_user(logged_user)

        flash('Usuario agregado exitosamente')
        return redirect(url_for('admin'))
    else:
        flash('¡Algo salió mal!')
        return redirect(url_for('admin'))
    
    # Eliminar - Ruta del botón --------->
@learntoApp.route('/delete/<int:id>')
def admin_delete(id):
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM user WHERE id = {0}".format(id))
        db.connection.commit()
        flash('Usuario eliminado exitosamente')
        return redirect(url_for('admin'))
    
    # Editar - Ruta del botón --------->
@learntoApp.route('/edit/<int:id>')
def admin_edit(id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE id = {0}".format(id))
    data = cursor.fetchall()
    
    # Editar - Actualización de los datos de usuario --------->
@learntoApp.route('/edit_update/<int:id>', methods = ['POST'])
def admin_edit_update(id):
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        fullname = request.form['fullname']
        age = request.form['age']
        schoolgrade = request.form['schoolgrade']
        auth = request.form['auth']
    cursor = db.connection.cursor()
    cursor.execute("""UPDATE user
    SET username = %s, email = %s, 
        fullname = %s, schoolgrade = %s,
        age = %s, auth = %s 
    WHERE id = %s""", (username, email, fullname, age, schoolgrade, auth))
    flash("Actualización de datos completada")
    return redirect(url_for('admin'))

    # ==============================
    # Registro
    # ==============================
@learntoApp.route('/loginRegister', methods=['GET', 'POST'])
def loginRegister():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        fullname = request.form['fullname']
        age = request.form['age']
        schoolgrade = request.form['schoolgrade']
        hash = generate_password_hash(password) 

        regUser = db.connection.cursor()
        query = "INSERT INTO user (username, email, password, fullname, age, schoolgrade) VALUES (%s, %s, %s, %s, %s, %s)"
        regUser.execute(query, (username, email, hash, fullname, age, schoolgrade))
        db.connection.commit()
        user = User(None, username, email, password, fullname, age, schoolgrade, None)
        logged_user = ModelUser.login(db, user)
        login_user(logged_user)
               
               
        email_subject = "Bienvenido a Learn To" 
        sender_email_address = "learntoapplication@gmail.com" 
        receiver_email_address = email 
        email_smtp = "smtp.gmail.com" 
        email_password = "fgdkyxtwwnjhuzvl" 
       # Create an email message object 
        message = EmailMessage() 
        # Configure email headers 
        message['Subject'] = email_subject 
        message['D-Corporation'] = sender_email_address 
        message['fullname'] = receiver_email_address 
        # Set email body text 
        message.set_content("Hola! Te damos la bienvenida a la plataforma de aprendizaje Aprender A") 
        # Set smtp server and port 
        server = smtplib.SMTP(email_smtp, '587') 
        # Identify this client to the SMTP server 
        server.ehlo() 
        # Secure the SMTP connection 
        server.starttls() 
        # Login to email account 
        server.login(sender_email_address, email_password) 
        # Send email 
        server.send_message(message) 
        # Close connection to server 
        server.quit()
        return render_template('homeUser.html')
    else:
        return render_template('loginRegister.html')

    # ==============================
    # Login
    # ==============================
@learntoApp.route('/loginUser', methods=['GET', 'POST'])
def loginUser():
    if request.method == 'POST':
        user = User(0, request.form['email'],  request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user is not None:
            if logged_user.password:
                login_user(logged_user)
                if logged_user.auth == 'A':
                    return redirect(url_for('admin'))
                else:
                    return render_template('homeUser.html')
            else:
                flash("Contraseña incorrecta...")
                return render_template('loginUser.html')
        else:
            flash("El usuario no se encuentra...")
            return render_template('loginUser.html')
    else:
            return render_template('loginUser.html')


@learntoApp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@learntoApp.route('/passwordRecovery')
def passwordR():
    return render_template('passwordRecovery.html')

def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    # return redirect(url_for('/index'))

@learntoApp.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"

@learntoApp.route("/homeUser")    
@login_required
def homeUser():
    return render_template('homeUser.html')

@learntoApp.route('/user')
@login_required
def user():
        if logged_user is not None:
            logged_user = ModelUser.login(db, user)
            return redirect(url_for('protected'))
        else:
            return render_template('user.html')

if __name__=='__main__':
    learntoApp.config.from_object(config['development'])
    learntoApp.config.update(DEBUG=True, SECRET_KEY="secret_sauce")
    csrf.init_app(learntoApp)
    # learntoApp.add_url_rule('/query_string', view_func=query_string)
    learntoApp.register_error_handler(404, pagina_no_encontrada)
    learntoApp.run(debug=True, port=3300)