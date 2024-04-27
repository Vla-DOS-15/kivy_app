from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        self.login_button = Button(text='Увійти', size_hint=(None, None), size=(150, 50))
        self.login_button.bind(on_press=self.on_login_press)
        layout.add_widget(self.login_button)

    def on_login_press(self, instance):
        self.manager.current = 'login'