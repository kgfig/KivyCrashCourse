from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput

class TutorialApp(App):

    # This method is automatically called when the App is run.
    # Whatever this returns is used as the root widget which is
    # automatically sized and positioned to fill the window.
    def build(self):
        box = BoxLayout(orientation='vertical')
        # Always size_hint_y to None so BoxLayout doesn't split the space proportionally and we can set the height manually
        textInput = TextInput(font_size=150, size_hint_y=None, height=200, text='Default')
        floatLayout = FloatLayout()
        scatter = Scatter()
        scatterText = Label(text="Default", font_size=150)

        # setter returns a function that sets the property with the given key
        textInput.bind(text=scatterText.setter('text'))

        floatLayout.add_widget(scatter)
        scatter.add_widget(scatterText)

        box.add_widget(textInput)
        box.add_widget(floatLayout)

        return box

if __name__ == '__main__':
    TutorialApp().run()
