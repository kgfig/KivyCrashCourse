from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter

class TutorialApp(App):

    # This method is automatically called when the App is run.
    # Whatever this returns is used as the root widget which is
    # automatically sized and positioned to fill the window.
    def build(self):
        floatLayout = FloatLayout()
        scatter = Scatter()
        scatterText = Label(text="Hello!", font_size=150)

        floatLayout.add_widget(scatter)
        scatter.add_widget(scatterText)
        
        return floatLayout

if __name__ == '__main__':
    TutorialApp().run()
