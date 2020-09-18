from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.fullscreen = False
class SigninWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        # self uzima ceo prozor SIGNINWINDOW i preko ID uzima polje
        user = self.ids.username_field # lista svih idejava i tacno username
        pwd = self.ids.pwd_field # lista svih idejava i tacno username
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname =='' or passw == '':
            info.text ='[color=#FF0000]Username and/ or password required[/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#00FF00]Logged in successfully !!![/color]'
class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__ == "__main__":
    sa = SigninApp()
    sa.run()