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

@learntoApp.route('/adminPage')
def admin():
    return render_template('admin.html')

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
        # ==============================
        # Mail
        # ==============================
        user = User(None, username, email, password, fullname, age, schoolgrade, None)
        logged_user = ModelUser.login(db, user)
        login_user(logged_user)
        
        server = smtplib.SMTP_SSL(host= 'smpt@gmail.com', port = 587)
        server = ehlo()
        server = starttls()
        server.login(user = 'learntoapplication@gmail.com', password = 'fgdkyxtwwnjhuzvl')
        mail_content = 'Prueba 1'
        server.sendmail(from_add = 'learntoapplication@gmail.com', to_addres = email, msg = mail_content)
        server.quit()
        return render_template('homeUser.html')

        return redirect("/loginUser")
    return render_template('loginRegister.html')


@learntoApp.route('/loginUser', methods=['GET', 'POST'])
def loginUser():
    if request.method == 'POST':
        user = User(0, request.form['email'],  request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                if logged_user == "A":
                    return redirect(url_for('sUsuario'))
                return redirect(url_for('homeUser'))
            else:
                flash("Contraseña incorrecta...")
                return render_template('loginUser.html')
        else:
            flash("El usuario no se encuentra...")
            return render_template('loginUser.html')
    else:
            return render_template('loginUser.html')

# ========================
# Login --- admin
# ========================
@learntoApp.route('/sUsuario', methods = ['GET', 'POST'])
def sUsuario():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM user")
    row = cursor.fetchall()
    return render_template('admin.html', user = row)

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

# @learntoApp.route('/homeUser')
# def homeUser():
#     login_required()
#     return redirect(url_for('homeUser'))

# @learntoApp.route('/user')
# def user():
#     login_required()
#     return redirect(url_for('user'))
    

if __name__=='__main__':
    learntoApp.config.from_object(config['development'])
    learntoApp.config.update(DEBUG=True, SECRET_KEY="secret_sauce")
    csrf.init_app(learntoApp)
    # learntoApp.add_url_rule('/query_string', view_func=query_string)
    learntoApp.register_error_handler(404, pagina_no_encontrada)
    learntoApp.run(debug=True, port=3300)