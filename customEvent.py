from kivy.app import App
from kivy.event import EventDispatcher
from kivy.uix.label import Label

class MyEventDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('on_test')
        super(MyEventDispatcher, self).__init__(**kwargs)

    def do_something(self, value):
        self.dispatch("on_test", value)

    def on_test(self, *args):
        print("I am dispatched", args)


def my_callback(value, *args):
    print("Hello, I got an event!", args)

class MyApp(App):
    def build(self):
        self.ev = MyEventDispatcher()
        self.ev.bind(on_test=my_callback)
        self.ev.do_something(["he", "llo"])
        return Label(text="Hello")

if __name__ == "__main__":
    MyApp().run() 
        