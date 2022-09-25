from multiprocessing import connection
from flask import Flask, render_template, session, url_for, request, redirect, jsonify
from werkzeug.security import generate_password_hash
# from flask-login import LoginManager(learntoApp)
from flask_mysqldb import MySQL
# import datetime
from config import config


# login_manager = LoginManager(learntoApp)

# app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

learntoApp = Flask(__name__)

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

def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    return redirect(url_for('home.html'))

if __name__=='__main__':
    learntoApp.config.from_object(config['development'])
    # learntoApp.add_url_rule('/query_string', view_func=query_string)
    learntoApp.register_error_handler(404, pagina_no_encontrada)
    learntoApp.run(debug=True, port=3300)

learntoApp.config["DEBUG"] = True
learntoApp.config["MYSQL_HOST"] = "localhost"
learntoApp.config["MYSQL_USER"] = "root"
learntoApp.config["MYSQL_PASSWORD"] = "mysql"
learntoApp.config["MYSQL_DB"] = "learnto"

conexion = MySQL(learntoApp)



@learntoApp.route('/loginRegister', methods=['GET', 'POST'])
def loginRegister():
    if request.method == 'POST':
        nameu = request.form['nameu']
        emailu = request.form['emailu']
        passwordu = request.form['passwordu']
        passwordencryption = generate_password_hash(passwordu)
        
        registerU = conexion.connection.cursor()
        registerU.execute("INSERT INTO usuario (nameu, emailu, passwordu), VALUES(%s, %s, %s)", (nameu, emailu, passwordu))
        conexion.connection.commit()
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

# def query_string():
#     print(request)
#     print(request.args)
#     print(request.args.get('param1'))
#     print(request.args.get('param2'))
#     return "Ok"

# @login_manager.user_loader
# def load_user(user_id):
#     for user in users:
#         if user.id == int(user_id):
#             return user
#     return None