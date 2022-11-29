from multiprocessing import connection
import re
from flask import Flask, render_template, session, url_for, request, redirect, jsonify, flash
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_mysqldb import MySQL
from datetime import datetime
from config import config
import smtplib
from smtplib import SMTPException
from threading import Thread
from flask_mail import Mail, Message
from email.message import EmailMessage
import os
# Models:
from models.modelUser import ModelUser

# Entities:
from models.entities.User import User

learntoApp = Flask(__name__)
learntoApp.config.from_object(config['development'])

# Objects: 
mail = Mail(learntoApp) 
csrf = CSRFProtect(learntoApp)
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
@learntoApp.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

@learntoApp.route('/admin-view', methods = ['GET', 'POST'])
@login_required
def admin_view():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    return render_template('admin-view.html', user = data)

@learntoApp.route('/admin-operations', methods = ['GET', 'POST'])
@login_required
def admin_operations():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    return render_template('admin-operations.html', user = data)

@learntoApp.route('/admin-articles-view', methods = ['GET', 'POST'])
@login_required
def articles_view():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM articles")
    data = cursor.fetchall()
    return render_template('articles-view.html', articles = data)

@learntoApp.route('/admin-articles-operations', methods = ['GET', 'POST'])
@login_required
def articles_operations():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM articles")
    data = cursor.fetchall()
    return render_template('articles-operations.html', articles = data)

    # Agregar artículo ------->

    # Agregar artículo - Ruta del botón --------->

    # Eliminar artículo ------->

    # Eliminar artículo - Ruta del botón --------->

    # Editar artículo ------->

    # Editar artículo - Ruta del botón --------->

    # Agregar usuario ------->

@learntoApp.route('/admin-comments-view', methods = ['GET', 'POST'])
@login_required
def comments_view():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM comments")
    data = cursor.fetchall()
    return render_template('comments-view.html', comments = data)

@learntoApp.route('/admin-comments-operations', methods = ['GET', 'POST'])
@login_required
def comments_operations():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM comments")
    data = cursor.fetchall()
    return render_template('comments-operations.html', comments = data)

    # Agregar comentario ------->

    # Agregar comentario - Ruta del botón --------->

    # Eliminar comentario ------->

    # Eliminar comentario - Ruta del botón --------->

    # Editar comentario ------->

    # Editar comentario - Ruta del botón --------->

@learntoApp.route('/login-admin', methods = ['GET', 'POST'])
@login_required
def login_admin():
    return render_template('login-admin.html')

    # Agregar usuario - Ruta del botón --------->
@learntoApp.route('/add', methods=['GET', 'POST'])
def admin_add():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        fullname = request.form['fullname']
        age = request.form['age']
        schoolgrade = request.form['schoolgrade']
        auth = request.form['auth']
        hash = generate_password_hash(password) 
        query = "INSERT INTO user (username, email, password, fullname, age, schoolgrade, auth, imgprofile) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        img = request.files['img']

        now = datetime.now()
        time = now.strftime("%Y%H%M%S")

        if img.filename !='':
            newNameFoto=time+img.filename
            img.save("Proyecto Aprender A/uploads/profile/"+newNameFoto)

        datos = (username, email, hash, fullname, age, schoolgrade, auth, newNameFoto)
        regUser = db.connection.cursor()
        regUser.execute(query, datos)
        db.connection.commit()
        
        msg = Message(subject="Bienvenido a Learn To", recipients=[email], html=render_template ("email-template.html"))
        mail.send(msg)
        flash('Usuario agregado exitosamente')
        return redirect(url_for('admin_operations'))
    else:
        flash('¡Algo salió mal!')
        return redirect(url_for('login-admin'))
    
    # Eliminar usuario - Ruta del botón --------->
@learntoApp.route('/delete/<int:id>')
def admin_delete(id):
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM user WHERE id = {0}".format(id))
        db.connection.commit()
        flash('Usuario eliminado exitosamente')
        return redirect(url_for('admin_operations'))
    
    # Editar usuario - Ruta del botón --------->
@learntoApp.route('/edit/<int:id>')
def admin_edit(id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE id = {0}".format(id))
    data = cursor.fetchall()
    
    # Editar - Actualización de los datos de usuario --------->
@learntoApp.route('/edit_update', methods = ['POST'])
def admin_edit_update():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        fullname = request.form['fullname']
        age = request.form['age']
        schoolgrade = request.form['schoolgrade']
        auth = request.form['auth']
        img = request.form['img']
        updateUser = db.connection.cursor()
        if password:
            hash= generate_password_hash(password)
            updateUser.execute("UPDATE user SET username = %s, email = %s, password = %s, fullname = %s, age = %s, schoolgrade = %s, auth = %s,  WHERE id = %s",(username, email, hash, fullname, age, schoolgrade, auth, id))
        else:
            updateUser.execute("UPDATE user SET username = %s, email = %s, fullname = %s, age = %s, schoolgrade = %s, auth = %s WHERE id = %s",(username, email, fullname, age, schoolgrade, auth, id))
        db.connection.commit()
    flash("Actualización de datos completada")
    return redirect(url_for('admin_operations'))

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

        msg = Message(subject="Bienvenido a Learn To", recipients=[email], html=render_template ("email-template.html"))
        mail.send(msg)
        return render_template('login.html')
    else:
        return render_template('login.html')

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
                return render_template('login.html')
        else:
            flash("El usuario no se encuentra...")
            return render_template('login.html')
    else:
            return render_template('login.html')


@learntoApp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@learntoApp.route('/passwordRecovery')
def passwordR():
    return render_template('passwordRecovery.html')

@learntoApp.errorhandler(404)
def errorhandler401(e):
    return render_template('404.html')

@learntoApp.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"

@learntoApp.route("/homeUser")    
@login_required
def homeUser():
    return render_template('homeUser.html')

@learntoApp.route('/perfilUser')
@login_required
def perfilUser():
    return render_template('perfilUser.html')

if __name__=='__main__':
    learntoApp.config.update(DEBUG=True, SECRET_KEY="secret_sauce")
    learntoApp.config['ALLOWED_IMAGE_EXTENSIONS'] = ['txt', 'pdf', 'JPEG','JPG','PNG','WEBP', 'GIF']
    learntoApp.run(debug=True, port=3300)