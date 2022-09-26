from .entities.User import User


class ModelUser():

    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT idu, nameu, fullname, emailu, passwordu FROM usuario
                    WHERE nameu = '{}'""".format(usuario.nameu)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                usuario = User(row[0], row[1], User.check_password(row[2], usuario.passwordu), row[3])
                return usuario
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, idu):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT idu, nameu, fullname FROM usuario WHERE idu = {}".format(idu)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)