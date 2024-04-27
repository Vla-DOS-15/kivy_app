from kivy.graphics import RoundedRectangle
from kivy.graphics.context_instructions import Color
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from Services.UserService import UserService

class LoginPage(Screen):

    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        server = '(localdb)\\mssqllocaldb'
        database = 'AccountingOfFamilyFinancesDB'
        self.user_manager = UserService(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};')


    def show_registration_form(self):
        self.ids.email_input.opacity = 1  # Показати поле для вводу електронної пошти
        self.ids.password_input.opacity = 1  # Показати поле для вводу пароля повторно
        self.ids.password_confirm_input.opacity = 1  # Показати поле для вводу пароля повторно
        # Тут ви також можете виконати інші дії, які потрібно зробити при виборі реєстрації
        self.ids.forgot_password_button.opacity = 0

        self.ids.btn_reg.bg_color = '#F5F5F5'  # Змінюємо колір фону через властивість bg_color
        self.ids.btn_reg.canvas.before.clear()  # Очищаємо попередні кольори
        self.ids.btn_reg.canvas.before.add(Color(0.482, 1, 0.439))  # Додаємо новий колір
        self.ids.btn_reg.canvas.before.add(
            RoundedRectangle(size=self.ids.btn_reg.size, pos=self.ids.btn_reg.pos, radius=[25]))  # Оновлюємо фон кнопки


        self.ids.btn_login.bg_color = '#F5F5F5'
        self.ids.btn_login.canvas.before.clear()  # Очищаємо попередні кольори
        self.ids.btn_login.canvas.before.add(Color(98,98,98))  # Додаємо новий колір
        self.ids.btn_login.canvas.before.add(
            RoundedRectangle(size=self.ids.btn_login.size, pos=self.ids.btn_login.pos, radius=[25]))



    def show_login_form(self):
        self.ids.email_input.opacity = 1  # Показати поле для вводу електронної пошти
        self.ids.password_input.opacity = 1  # Показати поле для вводу пароля
        self.ids.password_confirm_input.opacity = 0  # Показати поле для вводу пароля
        self.ids.forgot_password_button.opacity = 1  # Показати поле для вводу пароля

        self.ids.btn_login.bg_color = '#F5F5F5'
        self.ids.btn_login.canvas.before.clear()  # Очищаємо попередні кольори
        self.ids.btn_login.canvas.before.add(Color(0.482, 1, 0.439))  # Додаємо новий колір
        self.ids.btn_login.canvas.before.add(
            RoundedRectangle(size=self.ids.btn_login.size, pos=self.ids.btn_login.pos, radius=[25]))

        self.ids.btn_reg.bg_color = '#F5F5F5'
        self.ids.btn_reg.canvas.before.clear()  # Очищаємо попередні кольори
        self.ids.btn_reg.canvas.before.add(Color(98, 98, 98))  # Додаємо новий колір
        self.ids.btn_reg.canvas.before.add(
            RoundedRectangle(size=self.ids.btn_reg.size, pos=self.ids.btn_reg.pos, radius=[25]))

    def register_user(self):
        email = self.ids.email_input.text
        password = self.ids.password_input.text
        if self.user_manager.register_user(email, password):
            print("User registered successfully")
        else:
            print("Failed to register user")

    def login_user(self):
        email = self.ids.email_input.text.strip()
        password = self.ids.password_input.text.strip()
        if self.user_manager.login_user(email, password):
            print("User logged in successfully")
        else:
            print("Failed to log in user")