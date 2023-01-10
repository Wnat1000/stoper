import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

Builder.load_file(
    'main.kv'
)


class MainWidget(BoxLayout):
    number = NumericProperty()
    okr = NumericProperty()

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)

        Clock.schedule_interval(self.increment_time, .1)

        self.increment_time(0)

        self.okr = 0

        self.okrtime = 0

    def increment_time(self, interval):
        self.number += .1

    def start(self):
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, .1)

    def stop(self):
        Clock.unschedule(self.increment_time)

    def okrazenie(self):
        self.okr = self.number - self.okrtime
        self.okrtime = self.number
        self.lbl.text = f"okrazenie: {self.okr} s\n"

    def reset(self):
        self.number = 0
        self.okr = 0
        self.okrtime = 0
        self.lbl.text = ""

class TimeApp(App):
    def build(self):
        return MainWidget()


TimeApp().run()
