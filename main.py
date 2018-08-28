from kivy.app import App
from kivy.uix.button import Button

class TutorialApp(App):

    # This method is automatically called when the App is run.
    # Whatever this returns is used as the root widget which is
    # automatically sized and positioned to fill the window.
    def build(self):
        return Button(text='Click me!', background_color=(0, 0, 1, 1), font_size=16)

if __name__ == '__main__':
    TutorialApp().run()
