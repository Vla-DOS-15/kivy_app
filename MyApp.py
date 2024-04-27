from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from LoginPage import LoginPage
from main import SimpleApp
Builder.load_file('start_page.kv')

class StartPage(Screen):
    pass
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartPage(name='start'))
        sm.add_widget(LoginPage(name='login'))


        return sm

if __name__ == '__main__':
    MyApp().run()