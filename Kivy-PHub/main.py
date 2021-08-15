import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="[u][b]Name: [/b][/u]", font_size=20, markup=True))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text="[i]Email: [/i]", font_size=25, markup=True))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text="[color=F2DAA9] Password: [/color]", font_size=30, markup=True))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

class MyApp(App):
    def build(self):
        return MyGrid()

MyApp().run()
