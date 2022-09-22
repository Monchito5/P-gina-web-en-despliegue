class config:

    SECRET_KEY = 'monchito5'

class DevelompentConfig(config):
    DEBUG = True
    MYSQL_HOST      = 'localhost'
    MYSQL_USER      = 'root'
    MYSQL_PASSWORD  = 'mysql'
    MYSQL_DB        = 'learnto'

config = {'Development' : DevelompentConfig}