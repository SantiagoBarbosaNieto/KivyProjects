import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)
        self.add_widget(Label(text = "Hey", pos_hint = {"Top": 0}))

        with self.canvas:
            Color(1,0,0,1,mode='rgba')
            Color(.1,.5,.8,1,mode='rgba')
            self.rect = Rectangle(pos=(0,0), size=(5,5))
    def on_touch_down(self, touch):
        
        
        self.rect.pos = touch.pos
        print("Mouse down", touch)

    def on_touch_move(self, touch):
        Color(1,0,0,1,mode='rgba')
        if(MyApp.lastMovePos == (0,0)):
            print(MyApp.lastMovePos)
            MyApp.lastMovePos = touch.pos
        else:
            with self.canvas:
                Line(points = (MyApp.lastMovePos[0],MyApp.lastMovePos[1], touch.pos[0],touch.pos[1]), width = 5)
            MyApp.lastMovePos = touch.pos
        self.rect.pos = touch.pos
        print("Mouse move", touch)

    def on_touch_up(self, touch):
        MyApp.lastMovePos = (0,0)
        print("Mouse up", touch)

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="This should be at the top"))
        self.add_widget(Label(text=""))
        self.add_widget(Touch())
        self.add_widget(Label(text="g"))
        self.add_widget(Label(text="g"))
        self.add_widget(Label(text="g"))


class MyApp(App):
    lastMovePos = (0,0)
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()