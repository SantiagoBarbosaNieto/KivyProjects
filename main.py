import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.core.window import Window


class Menu(GridLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.cols = 3

        self.clearcolor = (1, 1, 1, 1)
        self.sliderR = Slider(min = 0, max = 255, value = int(MyApp.color.r*255))
        self.sliderG = Slider(min = 0, max = 255, value = int(MyApp.color.g*255))
        self.sliderB = Slider(min = 0, max = 255, value = int(MyApp.color.b*255))
        self.sliderA = Slider(min = 0, max = 255, value = int(MyApp.color.a*255))
        self.sliderW = Slider(min = 1, max = 100, value = 10)

        self.back = Rectangle()


        self.sliderR.bind(value = self.on_valueR)
        self.sliderG.bind(value = self.on_valueG)
        self.sliderB.bind(value = self.on_valueB) 
        self.sliderA.bind(value = self.on_valueA)
        self.sliderW.bind(value = self.on_valueW)

        self.sliderRValue = Label(text = str(self.sliderR.value))
        self.sliderGValue = Label(text = str(self.sliderG.value))
        self.sliderBValue = Label(text = str(self.sliderB.value))
        self.sliderAValue = Label(text = str(self.sliderA.value))
        self.sliderWValue = Label(text = str(self.sliderW.value))


        self.add_widget(Label(text = "R: "))
        self.add_widget(self.sliderR)
        self.add_widget(self.sliderRValue)
        self.add_widget(Label(text = "G: "))
        self.add_widget(self.sliderG)
        self.add_widget(self.sliderGValue)
        self.add_widget(Label(text = "B: "))
        self.add_widget(self.sliderB)
        self.add_widget(self.sliderBValue)
        self.add_widget(Label(text = "A: "))
        self.add_widget(self.sliderA)
        self.add_widget(self.sliderAValue)
        self.add_widget(Label(text = "Width: "))
        self.add_widget(self.sliderW)
        self.add_widget(self.sliderWValue)


    def on_valueR(self,instance, value):
        self.sliderRValue.text = "% d"% value
        MyApp.color = Color(float(value/255),MyApp.color.g,MyApp.color.b, MyApp.color.a, mode = 'rgba')
    def on_valueG(self,instance, value):
        self.sliderGValue.text = "% d"% value
        MyApp.color = Color(MyApp.color.r,float(value/255), MyApp.color.b, MyApp.color.a, mode = 'rgba')
    def on_valueB(self,instance, value):
        self.sliderBValue.text = "% d"% value
        MyApp.color = Color(MyApp.color.r, MyApp.color.g,float(value/255), MyApp.color.a, mode = 'rgba')
    def on_valueA(self,instance, value):
        self.sliderAValue.text = "% d"% value
        MyApp.color = Color(MyApp.color.r, MyApp.color.g,MyApp.color.b, float(value/255), mode = 'rgba')
    def on_valueW(self, instance, value):
        self.sliderWValue.text = "% d"% value
        MyApp.width = value


class Canvas(Widget):
    def __init__(self, **kwargs):
        super(Canvas, self).__init__(**kwargs)

    def on_touch_down(self,touch):

        with self.canvas:   
            Color(MyApp.color.r,MyApp.color.g,MyApp.color.b,MyApp.color.a, mode = "rgba")
            Line(points = (touch.pos[0],touch.pos[1], touch.pos[0]+1,touch.pos[1]+1), width = int(MyApp.width))
        MyApp.lastMovePos = touch.pos
        print("Mouse down", touch)

    def on_touch_move(self, touch):
        print("Mouse move", touch)
        if(MyApp.lastMovePos == (0,0)):
            print(MyApp.lastMovePos)
            MyApp.lastMovePos = touch.pos
        else:
            with self.canvas:
                Color(MyApp.color.r,MyApp.color.g,MyApp.color.b,MyApp.color.a, mode = "rgba")
                Line(points = (MyApp.lastMovePos[0],MyApp.lastMovePos[1], touch.pos[0],touch.pos[1]), width = int(MyApp.width))
            MyApp.lastMovePos = touch.pos

    def on_touch_up(self, touch):
        MyApp.lastMovePos = (0,0)
        print("Mouse up", touch)
        

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.rows = 2
        self.add_widget(Canvas(size_hint_y = None, height=Window.size[1]*0.8))
        self.add_widget(Menu())


 
class MyApp(App):
    color = Color(0.3,0.5,0,1,mode= 'rgba')
    lastMovePos = (0,0)
    width = 5
    def build(self):
        return MyGrid()



if __name__ == "__main__":
    MyApp().run()