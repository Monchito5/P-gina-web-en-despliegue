from multiprocessing import connection
import smtplib
import re
from flask import Flask, render_template, session, url_for, request, redirect, jsonify, flash
from werkzeug.security import generate_password_hash
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_mysqldb import MySQL
import datetime
from config import config

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

@learntoApp.route('/edit/<int:id>')
def admin_edit(id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE id = {0}".format(id))
    data = cursor.fetchall()


@learntoApp.route('/Iadmin', methods = ['POST', 'GET'])
def admin_new():
    if request.method=='POST':
        username = request.form['username']
        email = request.form['email']
        fullname = request.form['fullname']
        age = request.form['age']
        schoolgrade = request.form['schoolgrade']      

        regUser = db.connection.cursor()
        regUser.execute("INSERT INTO user (username, email, fullname, age, schoolgrade) VALUES (%s, %s, %s, %s, %s)", (username, email, fullname, age, schoolgrade))
        db.connection.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(request.url)

@learntoApp.route('/delete/<int:id>')
def admin_delete(id):
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM user WHERE id = {0}".format(id))
        db.connection.commit()
        flash('Usuario eliminado exitosamente')
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

        # Mail
        user = User(None, username, email, password, fullname, age, schoolgrade, None)
        logged_user = ModelUser.login(db, user)
        login_user(logged_user)
        
        server = smtplib.SMTP_SSL(host= 'smpt@gmail.com', port = 587)
        server.ehlo()
        server.starttls()
        server.login(user = 'learntoapplication@gmail.com', password = 'fgdkyxtwwnjhuzvl')
        mensaje = 'Prueba 1'
        server.sendmail(from_add = 'learntoapplication@gmail.com', to_addres = email, msg = mensaje)
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
        authUser = ModelUser.login(db, user)
        if authUser is not None:
            if authUser.password:
                login_user(authUser)
                if authUser.auth == 'A':
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
    return redirect(url_for('/index'))

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
    return render_template('user.html')

if __name__=='__main__':
    learntoApp.config.from_object(config['development'])
    learntoApp.config.update(DEBUG=True, SECRET_KEY="secret_sauce")
    csrf.init_app(learntoApp)
    # learntoApp.add_url_rule('/query_string', view_func=query_string)
    learntoApp.register_error_handler(404, pagina_no_encontrada)
    learntoApp.run(debug=True, port=3300)