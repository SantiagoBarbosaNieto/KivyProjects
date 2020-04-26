import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.core.window import Window


class Menu(GridLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)

        self.clearcolor = (1, 1, 1, 1)
        self.cols = 1
        self.btnColor = Button(text="Line Color")
        self.lblWidth = Label(text = "Width:")
        self.inputWidth = TextInput(text = str(MyApp.width), multiline = False)


        self.add_widget(Label(text = ""))
        self.add_widget(self.btnColor)
        self.add_widget(Label(text = ""))
        self.add_widget(self.lblWidth)
        self.add_widget(self.inputWidth)



class Canvas(Widget):
    def __init__(self, **kwargs):
        super(Canvas, self).__init__(**kwargs)
        self.add_widget(Label(text = "Hey", pos_hint = {"Top": 0}))

        with self.canvas:
            Color(1,1,1,1,mode='rgba')
            Color(.1,.5,.8,1,mode='rgba')


    def on_touch_down(self,touch):

        with self.canvas:   
            MyApp.color
            Line(points = (touch.pos[0],touch.pos[1], touch.pos[0]+1,touch.pos[1]+1), width = int(MyApp.width))
        MyApp.lastMovePos = touch.pos
        print("Mouse down", touch)

    def on_touch_move(self, touch):
        print("Mouse move", touch)
        Color(1,0,0,1,mode='rgba')
        if(MyApp.lastMovePos == (0,0)):
            print(MyApp.lastMovePos)
            MyApp.lastMovePos = touch.pos
        else:
            with self.canvas:
                MyApp.color
                Line(points = (MyApp.lastMovePos[0],MyApp.lastMovePos[1], touch.pos[0],touch.pos[1]), width = int(MyApp.width))
            MyApp.lastMovePos = touch.pos

    def on_touch_up(self, touch):
        MyApp.lastMovePos = (0,0)
        print("Mouse up", touch)
        

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Canvas())
        self.add_widget(Menu())


 
class MyApp(App):
    color = Color(1,1,0,1,mode= 'rgba')
    lastMovePos = (0,0)
    width = 5
    def build(self):
        return MyGrid()



if __name__ == "__main__":
    MyApp().run()