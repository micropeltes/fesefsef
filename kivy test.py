from kivy.app import App
from kivy.uix.label import Label

class App(App):
    def build(self):
        l = Label(text="awikwok",font_size=100)
        return l
if __name__ == '__main__':
    App().run()