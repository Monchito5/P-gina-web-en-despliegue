from flask import Flask, render_template, session, url_for

learntoApp = Flask(__name__)

@learntoApp.route('/')
def index():
    return render_template('home.html')

@learntoApp.route('/login')
def login():
    return render_template('login.html')

@learntoApp.route('/user/<nombre>')
def user(nombre):
    data={
        'titulo':'Usuario',
        'nombre':nombre
    }
    return render_template('user.html', data=data)

if __name__=='__main__':
    learntoApp.run(debug=True, port=3300)