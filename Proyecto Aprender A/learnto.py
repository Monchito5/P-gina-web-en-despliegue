from multiprocessing import connection
import re
from flask import Flask, render_template, session, url_for, request, redirect, jsonify, flash, send_from_directory
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
folder = os.path.join('/Proyecto Aprender A/uploads/profile')
learntoApp.config['folder'] = folder

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

@learntoApp.route('/Proyecto Aprender A/uploads/profile/<imgprofile>')
def uploads(imgprofile):
    return send_from_directory(learntoApp.config['folder'], imgprofile)

@learntoApp.route('/')
def index():        
    cursor = db.connection.cursor()
    cursor.execute("SELECT u.username FROM articles a JOIN user u ON u.id = a.ida WHERE a.id = 1")
    data_articles = cursor.fetchall()
    return render_template('home.html', user = data_articles)
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

@learntoApp.route('/add-admin', methods = ['GET', 'POST'])
@login_required
def login_admin():
    return render_template('add-admin.html')

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
        return redirect(url_for('add-admin'))
    
    # Eliminar usuario - Ruta del botón --------->
@learntoApp.route('/delete-user/<int:id>')
def admin_delete(id):
        cursor = db.connection.cursor()
        # cursor.execute("SELECT imgprofile FROM user WHERE id=%s", id)
        # fila=cursor.fetchall()
        # os.remove(os.path.join(learntoApp.config['folder'],fila[0][0]))
        # cursor.execute("DELETE FROM user WHERE id=%s",(id,))
        cursor.execute("SELECT * FROM user WHERE id = {0}".format(id))
        db.connection.commit()
        flash('Usuario eliminado exitosamente')
        return redirect(url_for('admin_operations'))
    
    # Editar usuario - Ruta del botón --------->
@learntoApp.route('/edit/<int:id>')
def admin_edit(id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE id = {0}".format(id))
    data = cursor.fetchall()
    return render_template('edit-admin.html', user = data)

    # Editar - Actualización de los datos de usuario --------->
@learntoApp.route('/edit-user', methods = ['POST'])
def admin_edit_update():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        fullname = request.form['fullname']
        age = request.form['age']
        schoolgrade = request.form['schoolgrade']
        auth = request.form['auth']
        hash = generate_password_hash(password) 
        updateUser = db.connection.cursor()
        query = "UPDATE user SET username = %s, email = %s, password = %s, fullname = %s, age = %s, schoolgrade = %s, auth = %s WHERE id = {0}".format(id);
        datos = (username, email, hash, fullname, age, schoolgrade, auth, id)

        # if request.files.get('img'):
        #     folder = '/Proyecto Aprender A/uploads/profile{}'.format(img)
        #     if os.path.exists(folder):
        #         os.remove(folder)
        #     img = request.files['img']
        #     filename = secure_filename(img.filename)
        #     img.save(os.path.join(learntoApp.config['folder'], filename))
        #     updateUser.execute("UPDATE user SET imgprofile = %s WHERE id = %s", (filename, id))

        # if password:
        #     hash = generate_password_hash(password) 
        #     updateUser.execute("UPDATE user SET username = %s, email = %s, password = %s, fullname = %s, age = %s, schoolgrade = %s, auth = %s, imgprofile = %s WHERE id = %s", (username, email, hash, fullname, age, schoolgrade, auth, id))
        # else:
        #     updateUser.excecute("UPDATE user SET username = %s, email = %s, fullname = %s, age = %s, schoolgrade = %s, auth = %s, imgprofile = %s WHERE id = %s", (username, email, hash, fullname, age, schoolgrade, auth, id))
        # img = request.files['img']        
        # now = datetime.now()
        # time = now.strftime("%Y%H%M%S")
        # query = "UPDATE user SET username = %s, email = %s, password = %s, fullname = %s, age = %s, schoolgrade = %s, auth = %s, imgprofile = %s WHERE id = %s";
        # datos = (username, email, hash, fullname, age, schoolgrade, auth, newNameFoto, id)
        
        # if img.filename !='':
        #     newNameFoto=time+img.filename
        #     img.save("Proyecto Aprender A/uploads/profile/"+newNameFoto)
            # updateUser.execute("SELECT imgprofile FROM user WHERE id=%s", id)
            # fila=updateUser.fetchall()

            # os.remove(os.path.join(learntoApp.config['folder'],fila[0][0]))
            # updateUser.execute("UPDATE user SET imgprofile=%s WHERE id=%s",(newNameFoto,id))
            # db.connection.commit()
        updateUser.execute(query, datos)
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
                    return redirect(url_for('homeUser'))
            else:
                flash("Contraseña incorrecta...")
                return render_template('login.html')
        else:
            flash("El usuario no se encuentra...")
            return render_template('login.html')
    else:
            return render_template('login.html')


@learntoApp.route('/perfilUser')
@login_required
def perfilUser():
    return render_template('perfilUser.html')

@learntoApp.route('/perfil-user-update')
def perfil_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        fullname = request.form['fullname']
        age = request.form['age']
        schoolgrade = request.form['schoolgrade']
        auth = request.form['auth']
        hash = generate_password_hash(password) 
        updateUser = db.connection.cursor()
        query = "UPDATE user SET username = %s, email = %s, password = %s, fullname = %s, age = %s, schoolgrade = %s, auth = %s WHERE id = {0}".format(id);
        datos = (username, email, hash, fullname, age, schoolgrade, auth, id)
        updateUser.execute(query, datos)
        db.connection.commit()
    flash("Actualización de datos completada")
    return redirect(url_for('perfilUser'))


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

@learntoApp.route("/homeUser")    
@login_required
def homeUser():
    return render_template('homeUser.html')



if __name__=='__main__':
    learntoApp.config.update(DEBUG=True, SECRET_KEY="secret_sauce")
    learntoApp.config['ALLOWED_IMAGE_EXTENSIONS'] = ['txt', 'pdf', 'JPEG','JPG','PNG','WEBP', 'GIF']
    learntoApp.run(debug=True, port=3300)