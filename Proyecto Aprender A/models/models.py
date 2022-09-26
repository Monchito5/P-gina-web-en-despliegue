from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):

    def __init__(self, idu, nameu, fullname, emailu, passwordu, is_admin=False):
        self.idu = idu
        self.nameu = nameu
        self.fullname = fullname
        self.emailu = emailu
        self.passwordu = generate_password_hash(passwordu)
        self.is_admin = is_admin

    def set_password(self, passwordu):
        self.password = generate_password_hash(passwordu)

    def check_password(self, passwordu):
        return check_password_hash(self.passwordu, passwordu)

    def __repr__(self):
        return '<User {}>'.format(self.emailu)

users = []

def get_user(emailu):
    for user in users:
        if user.email == emailu:
            return user
    return None