class config:
    SECRET_KEY = 'monchito5'

class DevelompentConfig(config):
    DEBUG = True
    MYSQL_HOST      = 'localhost'
    MYSQL_USER      = 'root'
    MYSQL_PASSWORD  = ''
    MYSQL_DB        = 'learnto'

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USERNAME = "learntoapplication@gmail.com"
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    MAIL_PASSWORD = "fgdkyxtwwnjhuzvl"
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

config = {'development' : DevelompentConfig}