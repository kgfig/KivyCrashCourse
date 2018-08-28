from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput

import random

class ScatterTextWidget(BoxLayout):

    def change_label_colour(self, *args):
        colour = [random.random() for i in range(3)] + [1]
        label = self.ids.my_label
        label.color = colour

class TutorialApp(App):

    # This method is automatically called when the App is run.
    # Whatever this returns is used as the root widget which is
    # automatically sized and positioned to fill the window.
    def build(self):
        return ScatterTextWidget()

if __name__ == '__main__':
    TutorialApp().run()
