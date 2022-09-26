from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, idu, nameu, passwordu, fullname="") -> None:
        self.id = id
        self.username = nameu
        self.password = passwordu
        self.fullname = fullname

    @classmethod
    def check_password(self, hashed_password, passwordu):
        return check_password_hash(hashed_password, passwordu)