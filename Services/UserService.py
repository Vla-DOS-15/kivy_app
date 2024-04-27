import pyodbc

class UserService:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def register_user(self, email, password):
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Users (Email, Password) VALUES (?, ?)", (email, password))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print("Error registering user:", e)
            return False

    def login_user(self, email, password):
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE Email = ? AND Password = ?", (email, password))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            return user is not None
        except Exception as e:
            print("Error logging in:", e)
            return False
