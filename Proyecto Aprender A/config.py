class config:

    SECRET_KEY = 'monchito5'

class DevelompentConfig(config):
    DEBUG = True
    MYSQL_HOST      = 'localhost'
    MYSQL_USER      = 'root'
    MYSQL_PASSWORD  = ''
    MYSQL_DB        = 'learnto'

config = {'development' : DevelompentConfig}