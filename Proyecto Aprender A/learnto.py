from flask import Flask, render_template, session, url_for

learntoApp = Flask(__name__)

@learntoApp.route('/')
def index():
    return render_template('home.html')

if __name__=='__main__':
    learntoApp.run(debug=True, port=3300)