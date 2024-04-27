from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button.button import MDButtonText
from LoginPage import LoginPage

Builder.load_file('start_page.kv')
Builder.load_file('login_page.kv')

Window.size = (350, 730)


class StartPage(Screen):
    pass


class PersonalRegistration(Screen):
    pass


class FamilyRegistration(Screen):
    pass


class SimpleApp(MDApp):
    def build(self):
        sm = ScreenManager()
        # Додано екрани
        sm.add_widget(StartPage(name='start'))
        sm.add_widget(LoginPage(name='login'))
        sm.add_widget(PersonalRegistration(name='personal_registration'))
        sm.add_widget(FamilyRegistration(name='family_registration'))
        # Прив'язка обробників подій до кнопок

        return sm

    def open_login_screen(self, instance):
        # Отримання екземпляра ScreenManager
        sm = App.get_running_app().root

        # Зміна активного екрану на 'login'
        sm.current = 'login'


if __name__ == '__main__':
    SimpleApp().run()
