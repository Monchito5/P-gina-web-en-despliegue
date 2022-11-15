import os
class config:
    SECRET_KEY = 'monchito5'
    MAIL_SERVER = 'smpt.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'learntoapplication@gmail.com'
    MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_CF')

class DevelompentConfig(config):
    DEBUG = True
    MYSQL_HOST      = 'localhost'
    MYSQL_USER      = 'root'
    MYSQL_PASSWORD  = ''
    MYSQL_DB        = 'learnto'

config = {'development' : DevelompentConfig}