from multiprocessing import connection
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

@learntoApp.route('/loginRegister', methods=['GET', 'POST'])
def loginRegister():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['email'])
        # print(request.form['password'])
        user = User(0,  request.form['fullname'], request.form['username'], request.form['email'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('index'))
            else:
                flash("Invalid password...")
                return render_template('loginRegister.html')
        else:
            flash("User not found...")
            return render_template('loginRegister.html')
    else:
            return render_template('loginRegister.html')


@learntoApp.route('/loginUser', methods=['GET', 'POST'])
def loginUser():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['username'],  request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('index'))
            else:
                flash("Invalid password...")
                return render_template('loginUser.html')
        else:
            flash("User not found...")
            return render_template('loginUser.html')
    else:
            return render_template('loginUser.html')

@learntoApp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# @learntoApp.route('/user/<nombre>')
# def user(nombre):
#     data={
#         'titulo':'Usuario',
#         'nombre':nombre
#     }
#     return render_template('user.html', data=data)

# def query_string():
#     print(request)
#     print(request.args)
#     print(request.args.get('param1'))
#     print(request.args.get('param2'))
#     return "Ok"

def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    return redirect(url_for('index'))

@learntoApp.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"

if __name__=='__main__':
    learntoApp.config.from_object(config['development'])
    learntoApp.config.update(DEBUG=True, SECRET_KEY="secret_sauce")
    csrf.init_app(learntoApp)
    # learntoApp.add_url_rule('/query_string', view_func=query_string)
    learntoApp.register_error_handler(404, pagina_no_encontrada)
    learntoApp.run(debug=True, port=3300)

# @login_manager.user_loader
# def load_user(user_id):
#     for user in users:
#         if user.id == int(user_id):
#             return user
#     return None