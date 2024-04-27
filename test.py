from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButtonSpeedDial


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return (
            MDScreen(
                MDFloatingActionButtonSpeedDial(
                    data={
                        'minus': 'handshake',
                        'PHP': 'language-php',
                        'C++': 'language-cpp',
                    },
                    root_button_anim=True,
                )
            )
        )


Example().run()