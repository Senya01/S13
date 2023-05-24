from lib.DBconn import con


class Client:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create(self):
        connection = con()
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM clients WHERE username = '{self.username}';")
            existing_client = cursor.fetchone()
            if existing_client:
                connection.close()
                return False
            else:
                cursor.execute(
                    f"INSERT INTO clients (username, password) VALUES ('{self.username}', MD5('{self.password}'));")
                connection.commit()
                connection.close()
                return True

    def login(self):
        connection = con()
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM clients WHERE username = '{self.username}' AND password = MD5({self.password});")
            existing_client = cursor.fetchone()
            connection.close()
            return existing_client
